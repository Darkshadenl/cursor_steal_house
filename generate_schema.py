import os
from crawl4ai.extraction_strategy import (
    JsonCssExtractionStrategy,
    JsonXPathExtractionStrategy,
)
from crawl4ai import LLMConfig
from dotenv import load_dotenv

load_dotenv()

# Sample HTML with product information
html = """
<html><head>
		<meta charset="UTF-8">
		<meta content="width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=1" name="viewport">
		
		<title>Van Heeswijkstraat , Udenhout | De Huissleutel - huren en verhuren in Tilburg</title>
		<base href="https://www.dehuissleutel.nl/">
		
		<meta name="description" content="...">
		<meta name="robots" content="index,follow">
		<meta name="theme-color" content="#AF9E43">
		
		<meta property="og:url" content="https://www.dehuissleutel.nl/nl/woning/3792/van-heeswijkstraat-26-a">
		<meta property="og:type" content="website">
		<meta property="og:locale" content="">
		<meta property="og:site_name" content="De Huissleutel - huren en verhuren in Tilburg">
		<meta property="og:title" content="Van Heeswijkstraat , Udenhout | De Huissleutel - huren en verhuren in Tilburg">
		<meta property="og:description" content="...">

				<meta property="og:image" content="https://www.dehuissleutel.nl/uploads/Haagdijk%20terras/h2.jpg">
				
		<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css"> 
		<link rel="stylesheet" type="text/css" href="css/jquery.fancybox.css" media="screen">
		<link rel="stylesheet" type="text/css" href="css/style.css?r=4">
		<link rel="stylesheet" type="text/css" href="css/responsive.css?r=4">
		<link rel="stylesheet" type="text/css" href="css/slick.css">
		<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css">
		
				
		<link rel="shortcut icon" type="image/png" href="https://www.dehuissleutel.nl/uploads/logo/favicon.png">
		<link rel="icon" type="image/png" href="https://www.dehuissleutel.nl/uploads/logo/favicon.png">
		<link rel="apple-touch-icon" href="https://www.dehuissleutel.nl/uploads/logo/favicon.png">
		<link rel="apple-touch-icon-precomposed" href="https://www.dehuissleutel.nl/uploads/logo/favicon.png">
		
					<link rel="alternate" hreflang="x-default" href="https://www.dehuissleutel.nl/Array">
							<link rel="alternate" hreflang="nl_NL" href="https://www.dehuissleutel.nl/nl">
							<link rel="alternate" hreflang="en_GB" href="https://www.dehuissleutel.nl/en">
					
				<link href="//fonts.googleapis.com/css?family=Work Sans:200,300,400,500,600,700,800?display=swap" rel="stylesheet" type="text/css">
				
		<style type="text/css">
		html, body, p, h1, h2, h3, h4, h5, h6, a, div, span, input, textarea, select {
			font-family: 'Work Sans', serif;
		}
		</style>
	<style id="monica-reading-highlight-style">
        .monica-reading-highlight {
          animation: fadeInOut 1.5s ease-in-out;
        }

        @keyframes fadeInOut {
          0%, 100% { background-color: transparent; }
          30%, 70% { background-color: rgba(2, 118, 255, 0.20); }
        }
      </style></head>
	<body cz-shortcut-listen="true" monica-id="ofpnmcalabcbjgholdjcjblkibolbppb" monica-version="7.9.1">
		
		<div class="site-container">
			
			<div class="header js-header">
				<div class="header-top">
					<div class="wrapper text-right">
													<a title="Quinten Meijboom" class="button--account button1 button--small pl-2 m-0 mr-1" href="nl/mijn-account"><i class="fas fa-user-circle larger align-text-bottom"></i><span>Quinten Meijboom</span></a>
							<a title="Uitloggen" class="button--account button3 button--small pl-2 m-0 mr-1" href="nl/uitloggen"><i class="fas fa-sign-out-alt align-text-bottm"></i><span>Uitloggen</span></a>
												
												<a class="button4 button--small pl-2 m-0" href="nl/reparatieverzoek">
							<i class="d-none d-sm-inline-block fas fa-tools align-text-bottm mr-1"></i>
							<span class="d-none d-sm-inline">Reparatieverzoek</span>
							<span class="d-inline d-sm-none">Reparatie</span>
						</a>
												
						<div class="language-picker-container">
	<div class="language-picker js-language-picker">
	    <div href="/nl" class="language-picker-item language-picker-item--first js-language-picker-current">
	        <div class="language-picker-icon">
	            <img src="/img/lang/nl.png" alt="">
	        </div>
	        <span class="d-none d-sm-inline-block">Nederlands</span>
	        <i class="language-picker-arrow fa fa-angle-down"></i>
	    </div>
	    	        	    	        	        <a href="/en/residence/3792/van-heeswijkstraat-26-a" class="language-picker-item">
	            <div class="language-picker-icon">
	                <img src="/img/lang/en.png" alt="">
	            </div>
	            <span class="d-none d-sm-inline-block">English</span>
	        </a>
	        	    	</div>
</div>					</div>
				</div>
				<div class="header-main">
					<div class="wrapper position-relative">
						<a class="header-logo" title="De Huissleutel - huren en verhuren in Tilburg" href="https://www.dehuissleutel.nl/nl">
							<img src="https://www.dehuissleutel.nl/uploads/logo/logo.png" alt="De Huissleutel - huren en verhuren in Tilburg">
						</a>
						<a class="button1 button--menu js-menu"><i class="fas fa-bars mr-2"></i>Menu</a>
			            <nav class="header-nav js-header-nav">
				            <a class="header-nav-close d-block d-lg-none js-menu" href="#">
					            <i class="fas fa-times"></i>
				            </a>
							                <ul>
	                	                		                	
						<li class="">
	                        <a href="nl/">
			                    Home			                    	                        </a>
			                						</li>
						                		                	
						<li class="active">
	                        <a href="nl/aanbod">
			                    Aanbod			                    	                        </a>
			                						</li>
						                		                	
						<li class="">
	                        <a>
			                    Diensten			                    			                    	<i class="fas fa-chevron-down fa-xs"></i>
			                    	                        </a>
			                	                        <ul>
		                        	                            <li class="">
	                                <a href="nl/diensten/woning-huren">
				                        Woning huren				                    </a>
	                            </li>
	                            	                            <li class="">
	                                <a href="nl/diensten/woning-verhuren">
				                        Woning verhuren				                    </a>
	                            </li>
	                            	                            <li class="">
	                                <a href="nl/diensten/vastgoedbeheer">
				                        Vastgoedbeheer				                    </a>
	                            </li>
	                            	                        </ul>
	                        						</li>
						                		                	
						<li class="">
	                        <a href="nl/hoe-werkt-het">
			                    Hoe werkt het?			                    	                        </a>
			                						</li>
						                		                	
						<li class="">
	                        <a href="nl/over-ons">
			                    Over ons			                    	                        </a>
			                						</li>
						                		                	
						<li class="">
	                        <a href="nl/vragen-faq">
			                    Vragen (FAQ)			                    	                        </a>
			                						</li>
						                		                	
						<li class="">
	                        <a href="nl/projecten">
			                    Projecten			                    	                        </a>
			                						</li>
						                		                	
						<li class="">
	                        <a href="nl/contact">
			                    Contact			                    	                        </a>
			                						</li>
					                </ul>			            </nav>
					</div>
				</div>
				
			</div>
			<div class="header-placeholder"></div>
			
							
<div class="wrapper my-5 text-box page-wrapper">

	    
    <div class="mb-4">
	    <h1 class="p-0 d-inline-block align-middle">
		    Van Heeswijkstraat  26-A, 5071CV Udenhout	    </h1>
		<div class="button1 button--noHover d-inline-block align-middle ml-3">€ 1.600,00 p/m excl. GWL</div>
    </div>
    
    <div class="row mb-5 is-in-viewport" data-inviewport="slide-in">
	    <div class="col-12 col-lg-8 mb-5 mb-lg-0">
		    <div class="image-slider-container">
			            			<div class="image-slider-item">
	        			<a href="https://www.dehuissleutel.nl/uploads/Haagdijk%20terras/h2.jpg" data-fancybox="thumbnail" style="background-image: url('https://www.dehuissleutel.nl/uploads/Haagdijk%20terras/h2.jpg');"></a>
        			</div>
	    			
	    			<div class="row row--smallGutter image-nav">
	        				        				        			    	                			<div class="col col-4 col-sm-4 image-nav-col">
	                    			<a class="image-nav-item" href="https://www.dehuissleutel.nl/uploads/Haagdijk%20terras/h6.jpg" data-fancybox="thumbnail" style="background-image:url('https://www.dehuissleutel.nl/uploads/Haagdijk%20terras/h6.jpg');">
	                        				                			    </a>
	                			</div>
	        			        	                        	        				        			    	                			<div class="col col-4 col-sm-4 image-nav-col">
	                    			<a class="image-nav-item" href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/16.jpg" data-fancybox="thumbnail" style="background-image:url('https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/16.jpg');">
	                        				                			    </a>
	                			</div>
	        			        	                        	        				        			    	                			<div class="col col-4 col-sm-4 image-nav-col">
	                    			<a class="image-nav-item" href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/21.jpg" data-fancybox="thumbnail" style="background-image:url('https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/21.jpg');">
	                        				                        			<div class="image-nav-item-overlay">+18</div>
	                        				                			    </a>
	                			</div>
	        			        	                        	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/22.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/17.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/18.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/19.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/4.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/5.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/7.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/8.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/11.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/10.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/14.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/23.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/25.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/28.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/28.jpg" data-fancybox="thumbnail"></a>
	        			    	        				        			    	        			        <a href="https://www.dehuissleutel.nl/uploads/Heeswijk%2026-a/31.jpg" data-fancybox="thumbnail"></a>
	        			    	        				    			</div>
	            		    </div>
	    </div>
	    <div class="col-12 col-lg-4">
		    		    
		    <iframe class="mb-4 map-iframe" width="100%" height="250" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?width=100%25&amp;height=250&amp;hl=en&amp;q=Van+Heeswijkstraat++26-A%2C+5071CV+Udenhout&amp;t=&amp;z=14&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"></iframe>
		    
		    		    <div class="card card--withFooter card--large card--dark">
			    <div class="card-section text-center">
				    <div class="page-icon mt-2 mb-2">
					    <i class="fas fa-calendar-check"></i>
				    </div>
				    <h4 class="text-white">Interesse in deze woonruimte?</h4>
				    				    <p>Klik op onderstaande knop om je aan te melden voor het kijkmoment.</p>
				    			    </div>
							    <div class="card-footer">
				    <button class="button1 m-0" data-toggle="modal" data-target="#subscribe-modal">aanmelden kijkmoment<i class="fas fa-arrow-right ml-2"></i></button>
			    </div>
			    		    </div>
		    	    </div>
    </div>
    <div class="row" data-inviewport="slide-in">
	    <div class="col-12 col-lg-8 mb-5 mb-lg-0">
		    <div class="card card--large card--withFooter">
			    <div class="card-section">
				    <h2>Over deze woonruimte</h2>
				    
				    <p>Per direct beschikbaar!</p>

<p>( twee personen kunnen zich registreren op dit adres )</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Open kijkavond:</p>

<p>Dinsdag 6 mei van 8.30 uur tot 9.00 uur. Aanmelden is niet nodig, u bent van harte welkom.</p>

<p>&nbsp;</p>

<p>Adres: Van Heeswijkstraat 26-A in Udenhout<br>
<br>
Appartement met eigen dakterras en eigen berging.<br>
<br>
Bezichtigen is op afspraak mogelijk, graag een mailtje sturen.<br>
<br>
Locatie:<br>
Het appartement ligt op ongeveer 6 minuten loopafstand van het centrum. Op korte afstand ( 150 meter ) is een supermarkt gelegen.&nbsp;<br>
<br>
Indeling:</p>

<p>Zeer ruime entreehal met trapopgang naar de eerste verdieping.</p>

<p>Eerste verdieping:</p>

<p>Ruime woonkamer met direct toegang tot een riant daktteras. Luxe- en grote open keuken. Het gehele appartement is voorzien van dubbel glas.</p>

<p>Ruime badkamer, welke is voorzien van een inloopdouche, 2 wastafels,&nbsp; spiegel en hangend toilet.&nbsp;</p>

<p>Slaapkamer met laminaatvloer ( enkel te bereiken via de badkamer ).</p>

<p>Tweede verdieping:</p>

<p>De tweede slaapkamer is op de zolderverdieping gelegen. Inpandige berging aanwezig met de wasmachine opstelling.</p>

<p>Berging:<br>
<br>
De toekomstige bewoners hebben de beschikking over een houten berging, voor bijvoorbeeld het veilig stallen van de fiets.&nbsp;</p>

<p><br>
Parkeren:<br>
<br>
In de buurt kan men gratis parkeren, zeer veel parkeergelegenheid.</p>

<p>Tevens heeft iedere bewoner een eigen parkeerplaats.<br>
<br>
Tv-signaal, internet, verlichting dienen door de toekomstige bewoner(s) zelf geregeld te worden.<br>
<br>
Bijzonderheden:<br>
<br>
- Minimale huurtermijn 12 maanden<br>
-&nbsp;Waarborgsom bedraagt 1,5 maand<br>
-&nbsp;Woonoppervlakte bedraagt ca. 102 m2<br>
- Honden/hondjes/katten zijn helaas niet toegestaan.<br>
- 2 aparte&nbsp;slaapkamers<br>
&nbsp;</p>

<p>Huurprijs:<br>
&nbsp;</p>

<p><br>
De huurprijs bedraagt EUR 1.600,00&nbsp; ( Exclusief verbruik gas, water, licht, internet, tv signaal en gemeentelijke belastingen. )</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p>Indien u geïnteresseerd bent in deze woning, kunt u zich inschrijven en direct contact opnemen met De Huissleutel tilburg@dehuissleutel.nl.&nbsp;</p>
				    
			    </div>
			    <div class="card-footer">
			        <a class="button1 m-0" href="nl/aanbod"><i class="fas fa-arrow-left mr-2"></i>Terug naar overzicht</a>
			    </div>
		    </div>
	    </div>
	    <div class="col-12 col-lg-4">
		    <div class="card card--highlighted">
			    <div class="card-section">
				    <h4 class="text-white">Details woonruimte</h4>
				    <div class="mt-2">
				        <div class="card-icon-container text-white">
					        <i class="fas fa-home"></i>
				        </div>
				        <div class="d-inline-block align-middle">Appartement</div>
			        </div>
			        <div class="mt-2">
				        <div class="card-icon-container text-white">
					        <i class="fas fa-map-marker-alt"></i>
				        </div>
				        <div class="d-inline-block align-middle">Nabij centrum</div>
			        </div>
			        <div class="mt-2">
				        <div class="card-icon-container text-white">
					        <i class="fas fa-expand"></i>
				        </div>
				        <div class="d-inline-block align-middle">102 m2</div>
			        </div>
			        <div class="mt-2">
				        <div class="card-icon-container text-white">
					        <i class="fas fa-bed fa-xs"></i>
				        </div>
				        <div class="d-inline-block align-middle">2 slaapkamers</div>
			        </div>
			        <div class="mt-2">
				        <div class="card-icon-container text-white">
					        <i class="fas fa-couch"></i>
				        </div>
				        <div class="d-inline-block align-middle">Gestoffeerd</div>
			        </div>
			        <div class="mt-2">
				        <div class="card-icon-container text-white">
					        <i class="fas fa-calendar-alt"></i>
				        </div>
				        <div class="d-inline-block align-middle">Aanvaarding: 23-04-2025</div>
			        </div>
			        <div class="mt-2">
				        <div class="card-icon-container text-white">
					        <i class="fas fa-euro-sign"></i>
				        </div>
				        <div class="d-inline-block align-middle">€ 1.600,00 p/m excl. GWL</div>
			        </div>
			        <div class="mt-2">
				        <div class="card-icon-container text-white">
					        <i class="fas fa-coins"></i>
				        </div>
				        <div class="d-inline-block align-middle">Borg: € 2.400</div>
			        </div>
			    </div>
		    </div>
	    </div>
    </div>
</div>


<form method="post" action="">
	<input type="hidden" name="mode" value="add_account_project_interest">
	<input type="hidden" name="project_id" value="3792">
	
	<div class="modal fade text-box" id="subscribe-modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
	  <div class="modal-dialog" role="document">
	    <div class="modal-content">
	      <div class="modal-header">
	        <h5 class="modal-title" id="exampleModalLabel">Weet je het zeker?</h5>
	        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
	          <span aria-hidden="true">×</span>
	        </button>
	      </div>
	      <div class="modal-body text-left">
	        Na het bevestigen van je interesse, wordt De Huissleutel op de hoogte gebracht en wordt er contact met je opgenomen over het kijkmoment.<br><br>Je gaat daarmee ook akkoord met de <a href="nl/voorwaarden-bezichtiging" target="_blank">voorwaarden van de bezichtiging</a>.	      </div>
	      <div class="modal-footer">
	        <button type="submit" class="button1">Bevestig interesse</button>
	      </div>
	    </div>
	  </div>
	</div>
</form>

<div class="u-light-bg py-5">
	<div class="wrapper text-box">
		<h2 class="text-center pb-2">Aanbod <span>van de Huissleutel</span></h2>
		
		<div class="pb-4 mb-2">
			<div class="project-slider js-project-slider slick-initialized slick-slider" data-inviewport="slide-in"><button type="button" data-role="none" class="slick-prev slick-arrow" aria-label="Previous" role="button" style=""><i class="fas fa-chevron-left"></i></button>
									<div aria-live="polite" class="slick-list draggable"><div class="slick-track" style="opacity: 1; width: 3700px; transform: translate3d(-1480px, 0px, 0px);" role="listbox"><div class="project-slider-item slick-slide slick-cloned" data-slick-index="-3" aria-hidden="true" style="width: 340px;" tabindex="-1">
					    <div class="card card--withFooter h-100">
    <div class="card-section">
                <a class="card-image" href="nl/woning/3574/koestraat-parkeerplaats" tabindex="-1">
            <div class="card-image-image" style="background-image:url('https://www.dehuissleutel.nl/uploads/aanbod/3574/3.jpg');"></div>
                    </a>
                
        <h5 class="pb-0">
            <a href="nl/woning/3574/koestraat-parkeerplaats" tabindex="-1">Koestraat, Tilburg</a>
        </h5>
        <h5 class="u-text-gold">€ 80,00 p/m excl. GWL</h5>
        <div class="mt-2">
	        <div class="card-icon-container">
		        <i class="fas fa-home"></i>
	        </div>
	        <div class="d-inline-block align-middle">Parkeerplaats</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-expand"></i>
	        </div>
	        <div class="d-inline-block align-middle">12 m2</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-bed fa-xs"></i>
	        </div>
	        <div class="d-inline-block align-middle">0 slaapkamers</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-calendar-alt"></i>
	        </div>
	        <div class="d-inline-block align-middle">Aanvaarding: 01-01-2025</div>
        </div>
    </div>
</div>
<div class="card-footer">
    <a class="button1 m-0" href="nl/woning/3574/koestraat-parkeerplaats" tabindex="-1">meer informatie<i class="fas fa-arrow-right ml-2"></i></a>
</div>					</div><div class="project-slider-item slick-slide slick-cloned" data-slick-index="-2" aria-hidden="true" style="width: 340px;" tabindex="-1">
					    <div class="card card--withFooter h-100">
    <div class="card-section">
                <a class="card-image" href="nl/woning/3350/haagdijk-zolder-45" tabindex="-1">
            <div class="card-image-image" style="background-image:url('https://www.dehuissleutel.nl/uploads/aanbod/3350/1.jpg');"></div>
                    </a>
                
        <h5 class="pb-0">
            <a href="nl/woning/3350/haagdijk-zolder-45" tabindex="-1">Haagdijk Zolder, Breda</a>
        </h5>
        <h5 class="u-text-gold">€ 549,00 p/m excl. GWL</h5>
        <div class="mt-2">
	        <div class="card-icon-container">
		        <i class="fas fa-home"></i>
	        </div>
	        <div class="d-inline-block align-middle">Studentenkamer</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-expand"></i>
	        </div>
	        <div class="d-inline-block align-middle">28 m2</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-bed fa-xs"></i>
	        </div>
	        <div class="d-inline-block align-middle">0 slaapkamers</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-calendar-alt"></i>
	        </div>
	        <div class="d-inline-block align-middle">Aanvaarding: 01-05-2025</div>
        </div>
    </div>
</div>
<div class="card-footer">
    <a class="button1 m-0" href="nl/woning/3350/haagdijk-zolder-45" tabindex="-1">meer informatie<i class="fas fa-arrow-right ml-2"></i></a>
</div>					</div><div class="project-slider-item slick-slide slick-cloned" data-slick-index="-1" aria-hidden="true" style="width: 340px;" tabindex="-1">
					    <div class="card card--withFooter h-100">
    <div class="card-section">
                <a class="card-image" href="nl/woning/3073/valentijnstraat-49" tabindex="-1">
            <div class="card-image-image" style="background-image:url('https://www.dehuissleutel.nl/uploads/Valentijn%20kamer4/1.jpg');"></div>
                    </a>
                
        <h5 class="pb-0">
            <a href="nl/woning/3073/valentijnstraat-49" tabindex="-1">Valentijnstraat , Tilburg</a>
        </h5>
        <h5 class="u-text-gold">€ 583,00 p/m excl. GWL</h5>
        <div class="mt-2">
	        <div class="card-icon-container">
		        <i class="fas fa-home"></i>
	        </div>
	        <div class="d-inline-block align-middle">Studentenkamer</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-expand"></i>
	        </div>
	        <div class="d-inline-block align-middle">22 m2</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-bed fa-xs"></i>
	        </div>
	        <div class="d-inline-block align-middle">0 slaapkamers</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-calendar-alt"></i>
	        </div>
	        <div class="d-inline-block align-middle">Aanvaarding: 01-05-2025</div>
        </div>
    </div>
</div>
<div class="card-footer">
    <a class="button1 m-0" href="nl/woning/3073/valentijnstraat-49" tabindex="-1">meer informatie<i class="fas fa-arrow-right ml-2"></i></a>
</div>					</div><div class="project-slider-item slick-slide" data-slick-index="0" aria-hidden="true" style="width: 340px;" tabindex="-1" role="option" aria-describedby="slick-slide00">
					    <div class="card card--withFooter h-100">
    <div class="card-section">
                <a class="card-image" href="nl/woning/3790/van-heeswijkstraat-26" tabindex="-1">
            <div class="card-image-image" style="background-image:url('https://www.dehuissleutel.nl/uploads/Haagdijk%20terras/h2.jpg');"></div>
                    </a>
                
        <h5 class="pb-0">
            <a href="nl/woning/3790/van-heeswijkstraat-26" tabindex="-1">Van Heeswijkstraat , Udenhout</a>
        </h5>
        <h5 class="u-text-gold">€ 1.750,00 p/m excl. GWL</h5>
        <div class="mt-2">
	        <div class="card-icon-container">
		        <i class="fas fa-home"></i>
	        </div>
	        <div class="d-inline-block align-middle">Appartement</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-expand"></i>
	        </div>
	        <div class="d-inline-block align-middle">110 m2</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-bed fa-xs"></i>
	        </div>
	        <div class="d-inline-block align-middle">1 slaapkamer</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-calendar-alt"></i>
	        </div>
	        <div class="d-inline-block align-middle">Aanvaarding: 01-04-2025</div>
        </div>
    </div>
</div>
<div class="card-footer">
    <a class="button1 m-0" href="nl/woning/3790/van-heeswijkstraat-26" tabindex="-1">meer informatie<i class="fas fa-arrow-right ml-2"></i></a>
</div>					</div><div class="project-slider-item slick-slide slick-current slick-active" data-slick-index="1" aria-hidden="false" style="width: 340px;" tabindex="-1" role="option" aria-describedby="slick-slide01">
					    <div class="card card--withFooter h-100">
    <div class="card-section">
                <a class="card-image" href="nl/woning/3574/koestraat-parkeerplaats" tabindex="0">
            <div class="card-image-image" style="background-image:url('https://www.dehuissleutel.nl/uploads/aanbod/3574/3.jpg');"></div>
                    </a>
                
        <h5 class="pb-0">
            <a href="nl/woning/3574/koestraat-parkeerplaats" tabindex="0">Koestraat, Tilburg</a>
        </h5>
        <h5 class="u-text-gold">€ 80,00 p/m excl. GWL</h5>
        <div class="mt-2">
	        <div class="card-icon-container">
		        <i class="fas fa-home"></i>
	        </div>
	        <div class="d-inline-block align-middle">Parkeerplaats</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-expand"></i>
	        </div>
	        <div class="d-inline-block align-middle">12 m2</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-bed fa-xs"></i>
	        </div>
	        <div class="d-inline-block align-middle">0 slaapkamers</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-calendar-alt"></i>
	        </div>
	        <div class="d-inline-block align-middle">Aanvaarding: 01-01-2025</div>
        </div>
    </div>
</div>
<div class="card-footer">
    <a class="button1 m-0" href="nl/woning/3574/koestraat-parkeerplaats" tabindex="0">meer informatie<i class="fas fa-arrow-right ml-2"></i></a>
</div>					</div><div class="project-slider-item slick-slide slick-active" data-slick-index="2" aria-hidden="false" style="width: 340px;" tabindex="-1" role="option" aria-describedby="slick-slide02">
					    <div class="card card--withFooter h-100">
    <div class="card-section">
                <a class="card-image" href="nl/woning/3350/haagdijk-zolder-45" tabindex="0">
            <div class="card-image-image" style="background-image:url('https://www.dehuissleutel.nl/uploads/aanbod/3350/1.jpg');"></div>
                    </a>
                
        <h5 class="pb-0">
            <a href="nl/woning/3350/haagdijk-zolder-45" tabindex="0">Haagdijk Zolder, Breda</a>
        </h5>
        <h5 class="u-text-gold">€ 549,00 p/m excl. GWL</h5>
        <div class="mt-2">
	        <div class="card-icon-container">
		        <i class="fas fa-home"></i>
	        </div>
	        <div class="d-inline-block align-middle">Studentenkamer</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-expand"></i>
	        </div>
	        <div class="d-inline-block align-middle">28 m2</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-bed fa-xs"></i>
	        </div>
	        <div class="d-inline-block align-middle">0 slaapkamers</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-calendar-alt"></i>
	        </div>
	        <div class="d-inline-block align-middle">Aanvaarding: 01-05-2025</div>
        </div>
    </div>
</div>
<div class="card-footer">
    <a class="button1 m-0" href="nl/woning/3350/haagdijk-zolder-45" tabindex="0">meer informatie<i class="fas fa-arrow-right ml-2"></i></a>
</div>					</div><div class="project-slider-item slick-slide slick-active" data-slick-index="3" aria-hidden="false" style="width: 340px;" tabindex="-1" role="option" aria-describedby="slick-slide03">
					    <div class="card card--withFooter h-100">
    <div class="card-section">
                <a class="card-image" href="nl/woning/3073/valentijnstraat-49" tabindex="0">
            <div class="card-image-image" style="background-image:url('https://www.dehuissleutel.nl/uploads/Valentijn%20kamer4/1.jpg');"></div>
                    </a>
                
        <h5 class="pb-0">
            <a href="nl/woning/3073/valentijnstraat-49" tabindex="0">Valentijnstraat , Tilburg</a>
        </h5>
        <h5 class="u-text-gold">€ 583,00 p/m excl. GWL</h5>
        <div class="mt-2">
	        <div class="card-icon-container">
		        <i class="fas fa-home"></i>
	        </div>
	        <div class="d-inline-block align-middle">Studentenkamer</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-expand"></i>
	        </div>
	        <div class="d-inline-block align-middle">22 m2</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-bed fa-xs"></i>
	        </div>
	        <div class="d-inline-block align-middle">0 slaapkamers</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-calendar-alt"></i>
	        </div>
	        <div class="d-inline-block align-middle">Aanvaarding: 01-05-2025</div>
        </div>
    </div>
</div>
<div class="card-footer">
    <a class="button1 m-0" href="nl/woning/3073/valentijnstraat-49" tabindex="0">meer informatie<i class="fas fa-arrow-right ml-2"></i></a>
</div>					</div><div class="project-slider-item slick-slide slick-cloned" data-slick-index="4" aria-hidden="true" style="width: 340px;" tabindex="-1">
					    <div class="card card--withFooter h-100">
    <div class="card-section">
                <a class="card-image" href="nl/woning/3790/van-heeswijkstraat-26" tabindex="-1">
            <div class="card-image-image" style="background-image:url('https://www.dehuissleutel.nl/uploads/Haagdijk%20terras/h2.jpg');"></div>
                    </a>
                
        <h5 class="pb-0">
            <a href="nl/woning/3790/van-heeswijkstraat-26" tabindex="-1">Van Heeswijkstraat , Udenhout</a>
        </h5>
        <h5 class="u-text-gold">€ 1.750,00 p/m excl. GWL</h5>
        <div class="mt-2">
	        <div class="card-icon-container">
		        <i class="fas fa-home"></i>
	        </div>
	        <div class="d-inline-block align-middle">Appartement</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-expand"></i>
	        </div>
	        <div class="d-inline-block align-middle">110 m2</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-bed fa-xs"></i>
	        </div>
	        <div class="d-inline-block align-middle">1 slaapkamer</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-calendar-alt"></i>
	        </div>
	        <div class="d-inline-block align-middle">Aanvaarding: 01-04-2025</div>
        </div>
    </div>
</div>
<div class="card-footer">
    <a class="button1 m-0" href="nl/woning/3790/van-heeswijkstraat-26" tabindex="-1">meer informatie<i class="fas fa-arrow-right ml-2"></i></a>
</div>					</div><div class="project-slider-item slick-slide slick-cloned" data-slick-index="5" aria-hidden="true" style="width: 340px;" tabindex="-1">
					    <div class="card card--withFooter h-100">
    <div class="card-section">
                <a class="card-image" href="nl/woning/3574/koestraat-parkeerplaats" tabindex="-1">
            <div class="card-image-image" style="background-image:url('https://www.dehuissleutel.nl/uploads/aanbod/3574/3.jpg');"></div>
                    </a>
                
        <h5 class="pb-0">
            <a href="nl/woning/3574/koestraat-parkeerplaats" tabindex="-1">Koestraat, Tilburg</a>
        </h5>
        <h5 class="u-text-gold">€ 80,00 p/m excl. GWL</h5>
        <div class="mt-2">
	        <div class="card-icon-container">
		        <i class="fas fa-home"></i>
	        </div>
	        <div class="d-inline-block align-middle">Parkeerplaats</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-expand"></i>
	        </div>
	        <div class="d-inline-block align-middle">12 m2</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-bed fa-xs"></i>
	        </div>
	        <div class="d-inline-block align-middle">0 slaapkamers</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-calendar-alt"></i>
	        </div>
	        <div class="d-inline-block align-middle">Aanvaarding: 01-01-2025</div>
        </div>
    </div>
</div>
<div class="card-footer">
    <a class="button1 m-0" href="nl/woning/3574/koestraat-parkeerplaats" tabindex="-1">meer informatie<i class="fas fa-arrow-right ml-2"></i></a>
</div>					</div><div class="project-slider-item slick-slide slick-cloned" data-slick-index="6" aria-hidden="true" style="width: 340px;" tabindex="-1">
					    <div class="card card--withFooter h-100">
    <div class="card-section">
                <a class="card-image" href="nl/woning/3350/haagdijk-zolder-45" tabindex="-1">
            <div class="card-image-image" style="background-image:url('https://www.dehuissleutel.nl/uploads/aanbod/3350/1.jpg');"></div>
                    </a>
                
        <h5 class="pb-0">
            <a href="nl/woning/3350/haagdijk-zolder-45" tabindex="-1">Haagdijk Zolder, Breda</a>
        </h5>
        <h5 class="u-text-gold">€ 549,00 p/m excl. GWL</h5>
        <div class="mt-2">
	        <div class="card-icon-container">
		        <i class="fas fa-home"></i>
	        </div>
	        <div class="d-inline-block align-middle">Studentenkamer</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-expand"></i>
	        </div>
	        <div class="d-inline-block align-middle">28 m2</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-bed fa-xs"></i>
	        </div>
	        <div class="d-inline-block align-middle">0 slaapkamers</div>
        </div>
        <div class="mt-1">
	        <div class="card-icon-container">
		        <i class="fas fa-calendar-alt"></i>
	        </div>
	        <div class="d-inline-block align-middle">Aanvaarding: 01-05-2025</div>
        </div>
    </div>
</div>
<div class="card-footer">
    <a class="button1 m-0" href="nl/woning/3350/haagdijk-zolder-45" tabindex="-1">meer informatie<i class="fas fa-arrow-right ml-2"></i></a>
</div>					</div></div></div>
									
									
									
							<button type="button" data-role="none" class="slick-next slick-arrow" aria-label="Next" role="button" style=""><i class="fas fa-chevron-right"></i></button></div>
		</div>
		
		<div class="text-center">
			<a href="nl/aanbod" class="button2 m-0">Bekijk het volledige huuraanbod</a>
		</div>
	</div>
</div>						
			<div class="footer text-box text-white">
	<div class="wrapper">
		<div class="row align-items-center">
			<div class="col-12 col-lg-2 text-center text-lg-left">
				<a class="footer-logo u-zoomOnHover" title="De Huissleutel - huren en verhuren in Tilburg" href="https://www.dehuissleutel.nl/nl">
					<img class="" src="https://www.dehuissleutel.nl/uploads/logo/logo.png" alt="De Huissleutel - huren en verhuren in Tilburg">
				</a>
			</div>
			<div class="col-12 col-lg-10 text-center text-lg-right pt-4 pt-lg-0">
				<span class="px-3">© 2025 De Huissleutel Tilburg</span>
								<span class="px-3"><a class="text-white" href="nl/algemene-voorwaarden">Algemene voorwaarden</a></span>
												<span class="px-3"><a class="text-white" href="nl/privacy-statement">Privacy Statement</a></span>
												<span class="px-3"><a class="text-white" href="nl/contact">Contact</a></span>
							</div>
		</div>
	</div>
</div>
		</div>
		
		<div class="modal fade" id="documentModal" tabindex="-1" role="dialog" aria-labelledby="documentModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="documentModalLabel">Van Heeswijkstraat , Udenhout</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">×</span>
        </button>
      </div>
      <div class="modal-body">
        Bezig met uploaden...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Sluiten</button>
      </div>
    </div>
  </div>
</div>


        		
		
                
        <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"></script>
		<script type="text/javascript" src="js/jquery.fancybox.js"></script>
		<script type="text/javascript" src="js/bootstrap.min.js"></script>
		<script type="text/javascript" src="js/slick.min.js"></script>
		<script type="text/javascript" src="js/script.js"></script>
		
		
				
				
					<script type="application/ld+json">
				[{"@context":"https:\/\/schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":null,"item":"https:\/\/www.dehuissleutel.nl\/\/"},{"@type":"ListItem","position":2,"name":null,"item":"https:\/\/www.dehuissleutel.nl\/"},{"@type":"ListItem","position":3,"name":null,"item":"https:\/\/www.dehuissleutel.nl\/van-heeswijkstraat-26-a"}]}]			</script>
				

	
	

<div id="monica-content-root" class="monica-widget" style="pointer-events: auto;"></div></body></html>
"""

google = os.getenv("GOOGLE_API_KEY")

# Option 1: Using OpenAI (requires API token)
css_schema = JsonCssExtractionStrategy.generate_schema(
    html,
    schema_type="css",
    query="""
Let op!
Ik ben alleen geïnteresseerd in alle tekst die bij 'over deze woonruimte' hoort, en 'details woonruimte'.
Daarnaast is er nog de knop 'aanmelden kijkmoment', waarvan ik de link interessant vindt.
    """,
    llm_config=LLMConfig(provider="gemini/gemini-2.0-flash-001", api_token=google),
)

# Use the generated schema for fast, repeated extractions
strategy = JsonCssExtractionStrategy(css_schema)

print(strategy.schema)
