provider "google" {
  project = var.project_id
  region  = var.region
}

variable "project_id" {
  description = "The Google Cloud project ID"
  type        = string
}

variable "region" {
  description = "The Google Cloud region"
  type        = string
  default     = "europe-west4"
}

# Create secrets from .env file
resource "google_secret_manager_secret" "steal_house_secrets" {
  for_each = {
    "POSTGRES_USER"     = "Database username"
    "POSTGRES_PASSWORD" = "Database password"
    "POSTGRES_DB"       = "Database name"
    "POSTGRES_HOST"     = "Database hostname or connection string"
    "DEEPSEEK_API_KEY"  = "DeepSeek API key"
    "GOOGLE_API_KEY"    = "Google API key for Gemini"
    "VESTEDA_EMAIL"     = "Vesteda login email"
    "VESTEDA_PASSWORD"  = "Vesteda login password"
  }

  secret_id = each.key
  
  replication {
    automatic = true
  }
  
  labels = {
    "application" = "steal-house"
  }
}

# Create service account for Cloud Run
resource "google_service_account" "steal_house_crawler" {
  account_id   = "steal-house-crawler"
  display_name = "StealHouse Crawler Service Account"
  description  = "Service account for the StealHouse crawler running in Cloud Run"
}

# Grant secret accessor role to service account
resource "google_secret_manager_secret_iam_member" "grant_secrets_access" {
  for_each = google_secret_manager_secret.steal_house_secrets

  secret_id = each.value.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.steal_house_crawler.email}"
}

# Create Cloud Run service
resource "google_cloud_run_service" "steal_house_crawler" {
  name     = "steal-house-crawler"
  location = var.region
  
  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/steal-house-crawler:latest"
        
        resources {
          limits = {
            cpu    = "1"
            memory = "2Gi"
          }
        }
        
        # Secret environment variables
        dynamic "env" {
          for_each = google_secret_manager_secret.steal_house_secrets
          
          content {
            name = env.key
            value_from {
              secret_key_ref {
                name = env.value.secret_id
                key  = "latest"
              }
            }
          }
        }
        
        # Regular environment variables
        env {
          name  = "POSTGRES_PORT"
          value = "5432"
        }
      }
      
      service_account_name = google_service_account.steal_house_crawler.email
      timeout_seconds      = 3600
    }
  }
  
  traffic {
    percent         = 100
    latest_revision = true
  }
  
  autogenerate_revision_name = true
}

# Cloud Scheduler job to trigger the crawler
resource "google_cloud_scheduler_job" "steal_house_crawler_job" {
  name        = "steal-house-crawler-job"
  description = "Triggers the StealHouse crawler daily"
  schedule    = "0 8 * * *"  # Run at 8 AM every day
  time_zone   = "Europe/Amsterdam"
  
  http_target {
    uri         = "${google_cloud_run_service.steal_house_crawler.status[0].url}/run"
    http_method = "POST"
    
    oidc_token {
      service_account_email = google_service_account.steal_house_crawler.email
    }
  }
} 