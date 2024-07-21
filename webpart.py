import base64
from io import BytesIO
import pickle
from sklearn.preprocessing import StandardScaler
import requests
import pandas as pd
from PIL import Image, UnidentifiedImageError
import streamlit as st
from streamlit_option_menu import option_menu
import json
import wikipedia 
import streamlit.components.v1 as components
import streamlit as st


#backgrounf image path
@st.cache_data
def get_image_as_base64(file):
    with open(file,"rb") as f:
        data=f.read()
    return base64.b64encode(data).decode()

img = get_image_as_base64("./images/mesh-1430108_1920.png")
smile_image=get_image_as_base64("./images/smilee.jpg")
man_image=get_image_as_base64("./images/result2.jpg")
fram_image=get_image_as_base64("./images/card.jpg")
diabatic_image=get_image_as_base64("./images/diabetics.jpg")
heart_image=get_image_as_base64("./images/manage.jpg")
about_us=get_image_as_base64("./images/about_us.jpg")
image1=get_image_as_base64("./images/image1.jpg")
image3=get_image_as_base64("./images/image2.jpg")
image2=get_image_as_base64("./images/image3.jpg")
sub1=get_image_as_base64("./images/sub1.png")
sub2=get_image_as_base64("./images/sub2.png")
sub3=get_image_as_base64("./images/sub3.png")
heathy_eating=get_image_as_base64("./images/healthy.jpg")
heart_test=get_image_as_base64("./images/heart_test.jpg")
result1=get_image_as_base64("./images/result1.jpg")
disease_test=get_image_as_base64("./images/disease_test.jpg")
card_test=get_image_as_base64("./images/cardio_test.jpg")
more_info=get_image_as_base64("./images/more_info.jpg")
prevent=get_image_as_base64("./images/prevention.jpg")
manage=get_image_as_base64("./images/manage.jpg")
excerise=get_image_as_base64("./images/exercide.jpg")
more_info2=get_image_as_base64("./images/more_info2.jpg")
more_info3=get_image_as_base64("./images/info3.jpg")
symptoms=get_image_as_base64("./images/symptoms.jpg")
healthy_living=get_image_as_base64("./images/healthy_living.jpg")
nutrition=get_image_as_base64("./images/nutrition.jpg")
risk_factore=get_image_as_base64("./images/risk_factors.jpg")
tips=get_image_as_base64("./images/tips.jpg")
peaks=get_image_as_base64("./images/exer.jpg")
history=get_image_as_base64("./images/history.jpg")
login=get_image_as_base64("./images/login.jpg")
sign=get_image_as_base64("./images/sign_up.jpg")
penu=get_image_as_base64("./images/penu.jpg")
penu_man=get_image_as_base64("./images/penu_man.jpg")
penu_result=get_image_as_base64("./images/penu_Result.jpg")
more_info4=get_image_as_base64("./images/more_info3.jpg")
penu_prev=get_image_as_base64("./images/pneu_prevention.jpg")
healthy_lungs=get_image_as_base64("./images/healthy_lungs.jpg")
medical_history=get_image_as_base64("./images/medical_his.png")

#main page heading 
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background: linear-gradient(325deg,#2C67F2 0%,#86fde8 68%,#9796f0 98%);
background-size: 180% 180%;
animation: gradient-animation 12s ease infinite;
}}
[data-testid="stHeader"]{{
background:rgb(2,0,36);
color:white;

}}
[data-testid="stHeader"] > div {{
right: 2rem;
}}
[data-testid="stSidebar"] {{
background: url("data:image/png;base64,{img}");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[id="disease-prediction-system"],[id="appointment-form"],[id="doctor-information:"],[id="test-history"],[id="login"],[id="sign-up"],[id="diabetes-prediction-using-ml"],[id="disease-prediction"]{{
    background:rgb(2,0,36);
    color:white;
    width:100%
    
}}

.element-container{{
background-color:rgba( 0, 0, 0, 0);
}}
.row{{display:flex;}}




@keyframes gradient-animation {{
  0% {{
    background-position: 0% 50%;
  }}
  50% {{
    background-position: 100% 50%;
  }}
  100% {{
    background-position: 0% 50%;
  }}
}}
</style>
"""
#hover effect on the cards
hover=f"""
<style>
@-webkit-keyframes ani {{
      from {{
        -webkit-mask-position: 0 0;
        mask-position: 0 0;
      }}
      to {{
        -webkit-mask-position: 100% 0;
        mask-position: 100% 0;
      }}
    }}

    @keyframes ani {{
      from {{
        -webkit-mask-position: 0 0;
        mask-position: 0 0;
      }}
      to {{
        -webkit-mask-position: 100% 0;
        mask-position: 100% 0;
      }}
    }}

    @-webkit-keyframes ani2 {{
      from {{
        -webkit-mask-position: 100% 0;
        mask-position: 100% 0;
      }}
      to {{
        -webkit-mask-position: 0 0;
        mask-position: 0 0;
      }}
    }}

    @keyframes ani2 {{
      from {{
        -webkit-mask-position: 100% 0;
        mask-position: 100% 0;
      }}
      to {{
        -webkit-mask-position: 0 0;
        mask-position: 0 0;
      }}
    }}                        
.card:hover,.featurette:hover{{
          -ms-transform: scale(1.01) !important; /* IE 9 */ 
          -webkit-transform: scale(1.01) !important; /* Safari 3-8 */
          transform: scale(1.01) !important;
          background:rgb(255,255,255,0.5) !important;
          margin:10px !important;
          color:black !important;              

          a-ms-transform: scale(1.01) !important;
          -webkit-transform: scale(1.01)!important;
          transform: scale(1.01)!important;
          background: rgba(255, 255, 255, 0.5)!important;
          -webkit-animation: ani2 0.7s steps(29) forwards !important;
 }}
 
.card:hover .card-title,
.card:hover .card-text {{
      color: black;
    }} 
.card:hover a{{
    color:rgba(0, 0, 238, 1)                    
}}  
</style>"""


bootstrap = f"""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<style>
        *{{
          background-color: transparent !important;
        }}
        .featurette{{
           background:rgb(2,0,36,0.7);
                       
           -webkit-mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
           mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
           -webkit-mask-size: 3000% 100%;
           mask-size: 3000% 100%; 
        
        }}
        .featurette:hover {{
          -ms-transform: scale(1.01) !important; /* IE 9 */ 
          -webkit-transform: scale(1.01) !important; /* Safari 3-8 */
          transform: scale(1.01) !important;
          background:rgb(255,255,255,0.5) !important;
          margin:10px !important;
          }}

        .featurette,.bd-placeholder-img{{
          margin:10px 10px 10px 5px !important;
        }}  
        .featurette-heading{{
        font-family:Impact, fantasy!important;
        }}
        
      </style>

<div id="myCarousel" class="carousel slide mb-6" data-bs-ride="carousel"style="background-color:rgba(0,0,0,0);">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="0" class="" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="1" aria-label="Slide 2" class="active" aria-current="true"></button>
      <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="2" aria-label="Slide 3" class=""></button>
    </div>
    <div class="carousel-inner" style="background-color:rgba(0,0,0,0);">
      <div class="carousel-item active carousel-item-start"style="background-color:rgba(0,0,0,0);">
        <img class="bd-placeholder-img" width="100%" height="100%" src="data:image/png;base64,{image1}"aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="var(--bs-secondary-color)"></rect></svg>
        <div class="container" style="background-color:rgba(0,0,0,0);">
          <div class="carousel-caption text-start" style="background-color:rgba(0,0,0,0);">
            <h1>DISEASE PREDICTION SYSTEM USING MACHINE LEARNING.</h1>
            <p class="opacity-75">A complete solution for disease.</p>
          </div>
        </div>
      </div>
      <div class="carousel-item carousel-item-next carousel-item-start" style="background-color:rgba(0,0,0,0);">
        <img class="bd-placeholder-img" width="100%" height="100%" src="data:image/png;base64,{image2}" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="var(--bs-secondary-color)"></rect></svg>
        <div class="container"style="background-color:rgba(0,0,0,0);">
          <div class="carousel-caption"style="background-color:rgba(0,0,0,0);">
            <h1>HEALTHY EATING AND EXERCISE PLAN.</h1>
            <p>Providing good eating and exercise habits for better physical and mental health.</p>
          </div>
        </div>
      </div>
      <div class="carousel-item" style="background-color:rgba(0,0,0,0);">
        <img class="bd-placeholder-img" width="100%" height="100%" src="data:image/png;base64,{image3}" aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false"><rect width="100%" height="100%" fill="var(--bs-secondary-color)"></rect></svg>
        <div class="container"style="background-color:rgba(0,0,0,0);">
          <div class="carousel-caption text-end" style="background-color:rgba(0,0,0,0);">
            <h1>PREVENTION AND MANAGMENT</h1>
            <p>Mesures which helps in disease prevention and management.</p>
          </div>
        </div>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>


    <!-- START THE FEATURETTES -->

    <hr class="featurette-divider">

<div class="row featurette">
  <div class="col-md-7">
    <h2 class="featurette-heading fw-normal lh-1">Predictive Disease Modeling: <span class="text-body-secondary">Harnessing Machine Learning for Early Detection and Prevention</span></h2>
    <p class="lead">This approach not only enables early intervention and personalized treatment plans but also empowers healthcare providers to allocate resources more efficiently, ultimately improving patient outcomes and public health strategies.</p>
    <ul class="list-unstyled">
      <li><strong>Early Intervention:</strong> Detect diseases at their earliest stages.</li>
      <li><strong>Personalized Treatment:</strong> Tailor treatment plans to individual patients.</li>
      <li><strong>Improved Outcomes:</strong> Enhance patient care and public health strategies.</li>
    </ul>
  </div>
  <div class="col-md-5">
    <a href="http://localhost:8501/?page=diabetes-prediction-using-ml">
      <img class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="450" height="400" src="data:image/png;base64,{sub1}" alt="Predictive Disease Modeling Image" role="img" aria-label="Predictive Disease Modeling Image" preserveAspectRatio="xMidYMid slice" focusable="false">
    </a>
  </div>
</div>


    <hr class="featurette-divider">

<div class="row featurette">
  <div class="col-md-7 order-md-2">
    <h2 class="featurette-heading fw-normal lh-1">Proactive Health Management: <span class="text-body-secondary">Providing Prevention Strategies and Vital Health Information</span></h2>
    <p class="lead">Proactive health management focuses on offering evidence-based prevention strategies and essential health information to individuals and communities.</p>
    <ul class="list-unstyled">
      <li><strong>Prevention Strategies:</strong> Utilize the latest research to prevent health issues before they arise.</li>
    </ul>
  </div>
  <div class="col-md-5 order-md-1">
    <img class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="100%" height="500" src="data:image/png;base64,{sub2}" role="img" aria-label="Health Management Image" alt="Proactive Health Management">
  </div>
</div>

    <hr class="featurette-divider">

    <div class="row featurette">
      <div class="col-md-7">
        <h2 class="featurette-heading fw-normal lh-1">Precision Health Insights:<span class="text-body-secondary">Delivering Highly Accurate Health Information.</span></h2>
        <p class="lead">Precision Health Insights is dedicated to delivering highly accurate health information, utilizing the latest advancements in medical research and technology.</p>
        <ul class="list-unstyled">
          <li><strong>Latest Research:</strong> Stay informed with cutting-edge medical research.</li>
          <li><strong>Technology-Driven:</strong> Benefit from the latest health technologies and innovations.</li>
        </ul>
      </div>
      <div class="col-md-5">
        <img class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="350" height="350" src="data:image/png;base64,{sub3}" role="img" aria-label="Placeholder: 500x500" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="var(--bs-secondary-bg)"></rect><text x="50%" y="50%" fill="var(--bs-secondary-color)" dy=".3em"></text></svg>
      </div>
    </div>
    <hr class="featurette-divider">

<div class="row featurette">
  <div class="col-md-7 order-md-2">
    <h2 class="featurette-heading fw-normal lh-1">User Health History and Guidance:<span class="text-body-secondary">Personalized Insights and Recommendations</span></h2>
    <p class="lead">Review your health history and receive personalized guidance based on your medical records and recent activities.</p>
    <!-- Guidance section -->
    <div id="guidance">
      <h3>Health Guidance</h3>   
      <ul>
        <li>Personal user medical history.</li>
        <li>Better insights for medical planning.</li>
        <li>Maintain a balanced diet rich in fruits and vegetables.</li>
      </ul>
    </div>
  </div>
  <div class="col-md-5  order-md-1">
    <img class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="100%" height="500" src="data:image/png;base64,{medical_history}" role="img" aria-label="User health history and guidance image" preserveAspectRatio="xMidYMid slice" focusable="false">
  </div>
</div>

    <hr class="featurette-divider">

    <!-- /END THE FEATURETTES -->

  </div><!-- /.container -->


<div class="row gy-3 gy-md-4 gy-lg-0 align-items-lg-center"  style="background-color:rgb(2,0,36) !important;
  color:white !important; margin:10px !important;">
      <div class="col-12 col-lg-6 col-xl-5">
        <img class="img-fluid rounded" loading="lazy" src="data:image/png;base64,{about_us}" alt="About 1">
      </div>
      <div class="col-12 col-lg-6 col-xl-7">
        <div class="row justify-content-xl-center">
          <div class="col-12 col-xl-11">
            <h2 class="mb-3">Who Are We?</h2>
            <p class="lead fs-4 text-secondary mb-3">We help people to build incredible brands and superior products. Our perspective is to furnish outstanding captivating services.</p>
            <p class="mb-4">We are a fast-growing company, but we have never lost sight of our core values. We believe in collaboration, innovation, and customer satisfaction. We are always looking for new ways to improve our products and services.</p>
            <div class="row gy-3 gy-md-0 gx-xxl-5X">
              <div class="col-12 col-md-6">
                <div class="d-flex">
                  <div class="me-4 text-primary">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
                      <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z" />
                    </svg>
                  </div>
                  <div style="margin:10px !important;">
                    <h2 class="h5 mb-3">Versatile Brand</h2>
                    <p class="text-secondary mb-0">We are crafting a digital method that subsists life across all mediums.</p>
                  </div>
                </div>
              </div>
              <div class="col-12 col-md-6">
                <div class="d-flex">
                  <div class="me-4 text-primary">
                    <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-fire" viewBox="0 0 16 16">
                      <path d="M8 16c3.314 0 6-2 6-5.5 0-1.5-.5-4-2.5-6 .25 1.5-1.25 2-1.25 2C11 4 9 .5 6 0c.357 2 .5 4-2 6-1.25 1-2 2.729-2 4.5C2 14 4.686 16 8 16Zm0-1c-1.657 0-3-1-3-2.75 0-.75.25-2 1.25-3C6.125 10 7 10.5 7 10.5c-.375-1.25.5-3.25 2-3.5-.179 1-.25 2 1 3 .625.5 1 1.364 1 2.25C11 14 9.657 15 8 15Z" />
                    </svg>
                  </div>
                  <div style="margin:10px !important;">
                    <h2 class="h5 mb-3">Digital Agency</h2>
                    <p class="text-secondary mb-0">We believe in innovation by merging primary with elaborate ideas.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>


<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
"""
first_page_image=f"""<style>
.many-disease-img {{
     width: 100% !important;
     display: block !important;
     margin: auto   !important;
}}
</style>
<img src="data:image/jpeg;base64,{disease_test}" class="many-disease-img" >
"""
second_page_image=f"""<style>
.diabetic-disease-img {{
     width: 100% !important;
     display: block !important;
     margin: auto   !important;
}}
</style>
<img src="data:image/jpeg;base64,{diabatic_image}" class="diabetic-disease-img" >
"""

third_page_image=f"""<style>
.heart-disease-img {{
     width: 100% !important;
     display: block !important;
     margin: auto   !important;
}}
</style>
<img src="data:image/jpeg;base64,{heart_test}" class="heart-disease-img" >
"""
forth_page_image=f"""<style>
.heart-disease-img {{
     width: 100% !important;
     display: block !important;
     margin: auto   !important;
}}
</style>
<img src="data:image/jpeg;base64,{card_test}" class="heart-disease-img" >
"""
#Result Pages
result_image1=f"""
<style>
.heart-disease-img {{
     width: 100% !important;
     height:500px !important;                   
     display: block !important;
     margin: auto   !important;
}}
</style>
<img src="data:image/jpeg;base64,{result1}" class="heart-disease-img" >
"""
result_if_page1=f"""<style>
/* Card styling */
.card {{
    width: 420px; /* Adjust width as needed */
    margin: 20px auto; /* Center the card horizontally */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add box shadow */
    border: 1px solid #ddd; /* Add border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Prevents image overflow */
    background:rgb(2,0,36,0.7);
                       
    -webkit-mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    -webkit-mask-size: 3000% 100%;
    mask-size: 3000% 100%;                    
}}

.card-img-top {{
    width: 100%; /* Full width image */
    height:200px; /* Maintain aspect ratio */
    object-fit: cover; /* Scale image while maintaining aspect ratio */
}}

.card-body {{
    padding: 20px; /* Padding inside the card body */
    height:200px;                    
}}

.card-title {{
    font-size: 1.25rem; /* Title font size */
    color:white; 
    margin-bottom: 10px; /* Space below title */
}}

.card-text {{
    font-size: 1rem; /* Text font size */
    color:white;                     
    line-height: 1.6; /* Line height */
}}
.card-text a{{
    color:red;
                        
}}

.btn-primary {{
    background-color: #007bff; /* Primary button background color */
    color: #fff; /* Text color */
    text-decoration: none; /* Remove underline */
    padding: 8px 16px; /* Button padding */
    border-radius: 4px; /* Rounded corners */
    display: inline-block; /* Display as inline block */
}}

.btn-primary:hover {{
    background-color: #0056b3; /* Button background color on hover */
}}

.btn-primary.disabled {{
    background-color: #ccc; /* Disabled button background color */
    cursor: not-allowed; /* Change cursor on disabled state */
}}
                    

/* Custom CSS for positioning */
.row {{
    display: flex; /* Use flexbox for layout */
}}

.col-left {{
    flex: 1; /* Take up 50%  =of the available space */
    padding-right: 10px; /* Optional: Add some spacing between cards */
}}
.col-middle {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}}                    

.col-right {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}}  
.sub-header{{
    text-align: center ! important;
    font-family:Impact, fantasy!important;                    
}}

                                                                                      
</style>

<h1 class="sub-header">Diabetes Information</h1>
                        
<p class="sub-header">Diabetes is a chronic condition that affects how your body turns food into energy.</p>      
<div class="row">   
    <div class="col-left">                        
        <div class="card">                
            <img src="data:image/jpeg;base64,{more_info}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">More Information</h5>   
                <p class="card-text">
                    Common symptoms of diabetes include frequent urination, increased thirst, extreme hunger, unexplained weight loss, fatigue, blurred vision, and slow wound healing.
                    <br>
                    <strong>Diabetes Overview:</strong> <a href="https://www.who.int/news-room/fact-sheets/detail/diabetes" target="_blank">More information about diabetes</a><br>
                </p>
            </div>
        </div>            
    </div>
    <div class="col-middle"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{manage}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Management</h5>
                <p class="card-text">
                    Managing diabetes involves a lifelong commitment to healthy living, regular medical care, and monitoring. With proper management, people can live healthy lives.
                    <br>
                    <strong>Diabetes Management:</strong> <a href="https://www.cdc.gov/diabetes/managing/index.html" target="_blank">How to manage Diabetes</a><br>
                </p>
            </div>
        </div>                  
    </div>                 
    <div class="col-right"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{prevent}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Prevention</h5>
                <p class="card-text">
                    Early detection and intervention are key to effective management and prevention of diabetes-related complications.
                    <br>
                    <strong>Preventing Diabetes:</strong> <a href="https://www.diabetes.org/diabetes-risk/prevention" target="_blank">How to prevent Diabetes</a><br>
                </p>
            </div>
        </div>                  
    </div>                  
</div>"""

no_disease_image=f"""
            <style>
            .heart-disease-img {{
                width: 1100px;
                height: 500px;
                display: block;
                margin: auto;
                padding-bottom:0px;
                                
                        
    
            }}
            </style>
            <img src="data:image/jpeg;base64,{smile_image}" class="heart-disease-img" >
            """
result_else_page1=f""" <style>
/* Card styling */
.card {{
    width: 500px; /* Adjust width as needed */
    margin: 20px auto; /* Center the card horizontally */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add box shadow */
    border: 1px solid #ddd; /* Add border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Prevents image overflow */
    background:rgb(2,0,36,0.7);
                       
    -webkit-mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    -webkit-mask-size: 3000% 100%;
    mask-size: 3000% 100%;                                                           
}}

.card-img-top {{
    width: 100%; /* Full width image */
    height: 200px; /* Maintain aspect ratio */
    object-fit: cover; /* Scale image while maintaining aspect ratio */
}}

.card-body {{
    padding: 20px; /* Padding inside the card body */
    height:430;                    
                        
}}

.card-title {{
    font-size: 1.25rem; /* Title font size */
    color:white; 
    margin-bottom: 10px; /* Space below title */
}}

.card-text {{
    font-size: 1rem; /* Text font size */
    color:white;                     
    line-height: 1.6; /* Line height */
}}
.card-text a{{
    color:red;
                        
}}

.btn-primary {{
    background-color: #007bff; /* Primary button background color */
    color: #fff; /* Text color */
    text-decoration: none; /* Remove underline */
    padding: 8px 16px; /* Button padding */
    border-radius: 4px; /* Rounded corners */
    display: inline-block; /* Display as inline block */
}}

.btn-primary:hover {{
    background-color: #0056b3; /* Button background color on hover */
}}

.btn-primary.disabled {{
    background-color: #ccc; /* Disabled button background color */
    cursor: not-allowed; /* Change cursor on disabled state */
}}
                    

/* Custom CSS for positioning */
.row {{
    display: flex; /* Use flexbox for layout */
}}

.col-left {{
    flex: 1; /* Take up 50%  =of the available space */
    padding-right: 10px; /* Optional: Add some spacing between cards */
}}

.col-right {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */                                   
}}  
.sub-header{{
    font-family:Impact, fantasy!important;                    
    text-align: center ! important;
}}                                     
</style>

<h1 class="sub-header">Healthy Life Information</h1>    
<p class="sub-header">The results indicate that you are not likely to have diabetes. However, it's always good to maintain a healthy lifestyle.</p>      
<div class="row">   
    <div class="col-left">                        
        <div class="card">                
            <img src="data:image/jpeg;base64,{heathy_eating}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Healthy Eating</h5>
                <p class="card-text">
                    Healthy eating plays a crucial role in maintaining overall health and well-being. It involves consuming a balanced diet that provides essential nutrients while avoiding excess calories and sugar.
                    <br>
                    <strong>Healthy Eating:</strong> <a href="https://www.healthline.com/nutrition/healthy-eating-tips" target="_blank">Healthy Eating Tips</a><br>
                </p>
            </div>
        </div>            
    </div>
    <div class="col-right"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{excerise}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Exercise</h5>
                <p class="card-text">
                    Regular physical activity is essential for maintaining physical and mental health. It offers numerous benefits beyond weight management and health.
                    <br>
                    <strong>Exercise:</strong> <a href="https://www.cdc.gov/physicalactivity/basics/pa-health/index.htm" target="_blank">Benefits of Regular Exercise</a><br>
                </p>
            </div>
        </div>                  
    </div>                  
</div>"""

result_page_image2=f"""
             <style>
            .heart-disease-img {{
                width: 1100px;
                height: 500px !important;
                display: block;
                margin: auto;
    
            }}
            </style>
            <img src="data:image/jpeg;base64,{man_image}" class="heart-disease-img" >
            """
heart_result_if=f""" <style>
/* Card styling */
.card {{
    width: 420px; /* Adjust width as needed */
                        
    margin: 20px auto; /* Center the card horizontally */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add box shadow */
    border: 1px solid #ddd; /* Add border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Prevents image overflow */
    background:rgb(2,0,36,0.7);
                       
    -webkit-mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    -webkit-mask-size: 3000% 100%;
    mask-size: 3000% 100%;                                        
}}

.card-img-top {{
    width: 100%; /* Full width image */
    height:200px; /* Maintain aspect ratio */
    object-fit: cover; /* Scale image while maintaining aspect ratio */
}}

.card-body {{
    padding: 20px; /* Padding inside the card body */
    height:230px;                    
}}

.card-title {{
    font-size: 1.25rem; /* Title font size */
    color:white; 
    margin-bottom: 10px; /* Space below title */
}}

.card-text {{
    font-size: 1rem; /* Text font size */
    color:white;                     
    line-height: 1.6; /* Line height */
}}
.card-text a{{
    color:red;
                        
}}

.btn-primary {{
    background-color: #007bff; /* Primary button background color */
    color: #fff; /* Text color */
    text-decoration: none; /* Remove underline */
    padding: 8px 16px; /* Button padding */
    border-radius: 4px; /* Rounded corners */
    display: inline-block; /* Display as inline block */
}}

.btn-primary:hover {{
    background-color: #0056b3; /* Button background color on hover */
}}

.btn-primary.disabled {{
    background-color: #ccc; /* Disabled button background color */
    cursor: not-allowed; /* Change cursor on disabled state */
}}
                    

/* Custom CSS for positioning */
.row {{
    display: flex; /* Use flexbox for layout */
}}

.col-left {{
    flex: 1; /* Take up 50%  =of the available space */
    padding-right: 10px; /* Optional: Add some spacing between cards */
}}
.col-middle {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}}                   

.col-right {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}} 
.sub-header{{
    text-align: center ! important;
    font-family:Impact, fantasy!important;                    
}}                                           
</style>

<h1 class="sub-header"> Heart Disease Information</h1>
<p class="sub-header">Heart disease refers to various types of heart conditions, with coronary artery disease being the most common.</p>    
<div class="row">   
    <div class="col-left">                        
        <div class="card">                
            <img src="data:image/jpeg;base64,{more_info2}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">More Information</h5>   
                <p class="card-text">
                   Heart problems encompass a wide range of conditions affecting the heart and blood vessels. Some of the most common heart conditions include heart attacks, heart failure, arrhythmias, and heart valve problems.
                    <br>
                    <strong>Heart Disease Overview:</strong> <a href="https://www.who.int/health-topics/cardiovascular-diseases" target="_blank">More information about heart problems</a><br>
                </p>
            </div>
        </div>            
    </div>
    <div class="col-middle"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{symptoms}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Symptoms</h5>
                <p class="card-text">
                   Understanding the symptoms, risk factors, and preventive measures for heart problems is crucial for maintaining heart health. Early detection, lifestyle modifications, and proper medical management can significantly reduce the risk of heart disease and improve overall quality of life.
                    <br>
                    <strong>Heart Disease Symptoms:</strong> <a href="(https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118" target="_blank">Symptoms of Heart Disease</a><br>
                </p>
            </div>
        </div>                  
    </div>                 
    <div class="col-right"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{prevent}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Prevention</h5>
                <p class="card-text">
                    Regular communication with healthcare providers is essential for personalized prevention and management strategies and  Prevention of heart problems involves adopting healthy lifestyle habits and managing risk factors effectively.
                    <br>
                    <strong>Preventing Heart Disease:</strong> <a href="https://www.cdc.gov/heartdisease/prevention.htm" target="_blank">How to prevent Heart Disease</a><br>
                </p>
            </div>
        </div>                  
    </div>                  
</div>"""

heart_page_else=f"""
                    <style>
/* Card styling */
.card {{
    width: 500px; /* Adjust width as needed */
    margin: 20px auto; /* Center the card horizontally */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add box shadow */
    border: 1px solid #ddd; /* Add border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Prevents image overflow */
    background:rgb(2,0,36,0.7);
                       
    -webkit-mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    -webkit-mask-size: 3000% 100%;
    mask-size: 3000% 100%;                    
}}

.card-img-top {{
    width: 100%; /* Full width image */
    height:200px; /* Maintain aspect ratio */
    object-fit: cover; /* Scale image while maintaining aspect ratio */
}}

.card-body {{
    padding: 20px; /* Padding inside the card body */
    height:200px;                    
}}

.card-title {{
    font-size: 1.25rem; /* Title font size */
    color:white; 
    margin-bottom: 10px; /* Space below title */
}}

.card-text {{
    font-size: 1rem; /* Text font size */
    color:white;                     
    line-height: 1.6; /* Line height */
}}
.card-text a{{
    color:red;
                        
}}

.btn-primary {{
    background-color: #007bff; /* Primary button background color */
    color: #fff; /* Text color */
    text-decoration: none; /* Remove underline */
    padding: 8px 16px; /* Button padding */
    border-radius: 4px; /* Rounded corners */
    display: inline-block; /* Display as inline block */
}}

.btn-primary:hover {{
    background-color: #0056b3; /* Button background color on hover */
}}

.btn-primary.disabled {{
    background-color: #ccc; /* Disabled button background color */
    cursor: not-allowed; /* Change cursor on disabled state */
}}
                    

/* Custom CSS for positioning */
.row {{
    display: flex; /* Use flexbox for layout */
}}

.col-left{{
    flex: 1; /* Take up 50%  =of the available space */
    padding-right: 10px; /* Optional: Add some spacing between cards */
}}

.col-right {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}}
.sub-header{{
    text-align: center ! important;
    font-family:Impact, fantasy!important;                    
}}                                            
</style>
                    
<h1 class="sub-header">Healthy Life Information</h1>
<p class="sub-header">The results indicate that you are not likely to have heart disease.but, Maintaining a healthy heart is crucial for overall health.</p>                    
<div class="row">   
    <div class="col-left">                        
        <div class="card">                
            <img src="data:image/jpeg;base64,{tips}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Healthy Heart Tips</h5>
                <p class="card-text">
                    Healthy heart plays a crucial role in maintaining overall health and well-being. It involves consuming a balanced diet that provides essential nutrients while avoiding excess calories and sugar.
                    <br>
                    <strong>Tips for a Healthy Heart:</strong> <a href="https://www.heart.org/en/healthy-living" target="_blank">Healthy heart tips</a><br>
                </p>
            </div>
        </div>            
    </div>                
    <div class="col-right"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{peaks}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Exercise and Heart Health</h5>
                <p class="card-text">
                    Regular physical activity is essential for maintaining physical and mental health. It offers numerous benefits beyond weight management.
                    <br>
                    <strong>Exercise and Heart Health:</strong> <a href="https://www.cdc.gov/physicalactivity/basics/pa-health/index.htm" target="_blank">Benefits of healthy heart</a><br>
                </p>
            </div>
        </div>                  
    </div>                  
</div>
"""
cardio_page_image=f"""
             <style>
            .heart-disease-img {{
                width: 1100px;
                height: 500px !important;
                display: block;
                margin: auto;
    
            }}
            </style>
            <img src="data:image/jpeg;base64,{fram_image}" class="heart-disease-img" >
            """
cardio_page_if=f""" <style>
/* Card styling */
.card {{
    width: 420px; /* Adjust width as needed */
    margin: 20px auto; /* Center the card horizontally */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add box shadow */
    border: 1px solid #ddd; /* Add border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Prevents image overflow */
    background:rgb(2,0,36,0.7);
                       
    -webkit-mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    -webkit-mask-size: 3000% 100%;
    mask-size: 3000% 100%;                                        
}}

.card-img-top {{
    width: 100%; /* Full width image */
    height:200px; /* Maintain aspect ratio */
    object-fit: cover; /* Scale image while maintaining aspect ratio */
}}

.card-body {{
    padding: 20px; /* Padding inside the card body */
    height:250px                    
}}

.card-title {{
    font-size: 1.25rem; /* Title font size */
    color:white; 
    margin-bottom: 10px; /* Space below title */
}}

.card-text {{
    font-size: 1rem; /* Text font size */
    color:white;                     
    line-height: 1.6; /* Line height */
}}
.card-text a{{
    color:red;
                        
}}

.btn-primary {{
    background-color: #007bff; /* Primary button background color */
    color: #fff; /* Text color */
    text-decoration: none; /* Remove underline */
    padding: 8px 16px; /* Button padding */
    border-radius: 4px; /* Rounded corners */
    display: inline-block; /* Display as inline block */
}}

.btn-primary:hover {{
    background-color: #0056b3; /* Button background color on hover */
}}

.btn-primary.disabled {{
    background-color: #ccc; /* Disabled button background color */
    cursor: not-allowed; /* Change cursor on disabled state */
}}
                    

/* Custom CSS for positioning */
.row {{
    display: flex; /* Use flexbox for layout */
}}

.col-left {{
    flex: 1; /* Take up 50%  =of the available space */
    padding-right: 10px; /* Optional: Add some spacing between cards */
}}
.col-middle {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}}                    

.col-right {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}}
.sub-header{{
    text-align: center ! important;
    font-family:Impact, fantasy!important;                    
}}                                           
</style>

<h1 class="sub-header">Cardiovascular Disease Information</h1>
<p class="sub-header">The Framingham Heart Study helps understand cardiovascular disease, including risk factors and prevention.</p>    
<div class="row">   
    <div class="col-left">                        
        <div class="card">                
            <img src="data:image/jpeg;base64,{more_info3}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">More Information</h5>   
                <p class="card-text">
                  The Framingham Heart Study identified several key risk factors for cardiovascular disease, including high blood pressure, high cholesterol levels, smoking, obesity, diabetes, and physical inactivity.
                    <br>
                    <strong>Framingham Heart Study Overview:</strong> <a href="https://www.framinghamheartstudy.org/" target="_blank">More information about Framingham</a><br>
                </p>
            </div>
        </div>            
    </div>
    <div class="col-middle"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{risk_factore}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Risk Factors</h5>
                <p class="card-text">
                   Several risk factors contribute to the development of cardiovascular disease, and managing these risk factors is crucial for prevention and treatment,Some risk factors are in the given link.
                    <br>
                    <strong>Cardiovascular Disease Risk Factors:</strong> <a href="(https://www.cdc.gov/heartdisease/risk_factors.htm" target="_blank">Risk Factors of Framingham</a><br>
                </p>
            </div>
        </div>                  
    </div>                 
    <div class="col-right"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{manage}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Management</h5>
                <p class="card-text">
                    Managing cardiovascular disease risk factors involves a multifaceted approach that includes lifestyle modifications, medications, regular monitoring, and addressing underlying health conditions. By taking proactive steps to control these risk factors. 
                    <br>
                    <strong>Managing Cardiovascular Disease:</strong> <a href="https://www.heart.org/en/health-topics/cardiovascular-conditions" target="_blank">How to Manage it</a><br>
                </p>
            </div>
        </div>                  
    </div>                  
</div>"""

cardio_page_else=f"""
                    <style>
/* Card styling */
.card {{
    width: 500px; /* Adjust width as needed */
    margin: 20px auto; /* Center the card horizontally */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add box shadow */
    border: 1px solid #ddd; /* Add border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Prevents image overflow */
    background:rgb(2,0,36,0.7);
                       
    -webkit-mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    -webkit-mask-size: 3000% 100%;
    mask-size: 3000% 100%;                                        
}}

.card-img-top {{
    width: 100%; /* Full width image */
    height: auto; /* Maintain aspect ratio */
    object-fit: cover; /* Scale image while maintaining aspect ratio */
}}

.card-body {{
    padding: 20px; /* Padding inside the card body */
    height:190px;                    
}}

.card-title {{
    font-size: 1.25rem; /* Title font size */
    color:white; 
    margin-bottom: 10px; /* Space below title */
}}

.card-text {{
    font-size: 1rem; /* Text font size */
    color:white;                     
    line-height: 1.6; /* Line height */
}}
.card-text a{{
    color:red;
                        
}}

.btn-primary {{
    background-color: #007bff; /* Primary button background color */
    color: #fff; /* Text color */
    text-decoration: none; /* Remove underline */
    padding: 8px 16px; /* Button padding */
    border-radius: 4px; /* Rounded corners */
    display: inline-block; /* Display as inline block */
}}

.btn-primary:hover {{
    background-color: #0056b3; /* Button background color on hover */
}}

.btn-primary.disabled {{
    background-color: #ccc; /* Disabled button background color */
    cursor: not-allowed; /* Change cursor on disabled state */
}}
                    

/* Custom CSS for positioning */
.row {{
    display: flex; /* Use flexbox for layout */
}}

.col-left {{
    flex: 1; /* Take up 50%  =of the available space */
    padding-right: 10px; /* Optional: Add some spacing between cards */
}}

.col-right {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}}
.sub-header{{
    text-align: center ! important;
    font-family:Impact, fantasy!important;                    
}}                                            
</style>
                    
<h1 class="sub-header">Healthy Life Information</h1>
<p class="sub-header">The results indicate that you are not likely to have cardiovascular disease. It's important to keep your heart healthy.</p>                    
<div class="row">   
    <div class="col-left">                        
        <div class="card">                
            <img src="data:image/jpeg;base64,{healthy_living}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Healthy Living</h5>
                <p class="card-text">
                    Healthy heart plays a crucial role in maintaining overall health and well-being.but, It involves consuming a balanced diet that provides essential nutrients while avoiding excess calories and sugar.
                    <br>
                    <strong>Living a Heart-Healthy Lifestyle:</strong> <a href="https://www.cdc.gov/heartdisease/healthy_living.htm" target="_blank">Healthy Lifestyle Tips</a><br>
                </p>
            </div>
        </div>            
    </div>                
    <div class="col-right"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{nutrition}" class="card-img-top" alt="Placeholder Image">
            <div class="card-body">
                <h5 class="card-title">Nutrition</h5>
                <p class="card-text">
                    Regular physical activity is essential for maintaining physical and mental health. It offers numerous benefits beyond weight management.
                    <br>
                    <strong>Heart-Healthy Nutrition:</strong> <a href="https://www.heart.org/en/healthy-living/healthy-eating" target="_blank">Benefits of Nutritions</a><br>
                </p>
            </div>
        </div>                  
    </div>                  
</div>
"""
penumonia_page_image=f"""
             <style>
            .heart-disease-img {{
                width: 1100px;
                height: 500px !important;
                display: block;
                margin: auto;
    
            }}
            </style>
            <img src="data:image/jpeg;base64,{penu}" class="heart-disease-img" >
            """
penumonia_result_image=f"""
             <style>
            .heart-disease-img {{
                width: 1100px;
                height: 500px !important;
                display: block;
                margin: auto;
    
            }}
            </style>
            <img src="data:image/jpeg;base64,{penu_result}" class="heart-disease-img" >
            """

penumonia_result_if=f""" <style>
/* Card styling */
.card {{
    width: 420px; /* Adjust width as needed */
                        
    margin: 20px auto; /* Center the card horizontally */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add box shadow */
    border: 1px solid #ddd; /* Add border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Prevents image overflow */
    background:rgb(2,0,36,0.7);
                       
    -webkit-mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    -webkit-mask-size: 3000% 100%;
    mask-size: 3000% 100%;                                        
}}

.card-img-top {{
    width: 100%; /* Full width image */
    height:200px; /* Maintain aspect ratio */
    object-fit: cover; /* Scale image while maintaining aspect ratio */
}}

.card-body {{
    padding: 20px; /* Padding inside the card body */
    height:230px;                    
}}

.card-title {{
    font-size: 1.25rem; /* Title font size */
    color:white; 
    margin-bottom: 10px; /* Space below title */
}}

.card-text {{
    font-size: 1rem; /* Text font size */
    color:white;                     
    line-height: 1.6; /* Line height */
}}
.card-text a{{
    color:red;
                        
}}

.btn-primary {{
    background-color: #007bff; /* Primary button background color */
    color: #fff; /* Text color */
    text-decoration: none; /* Remove underline */
    padding: 8px 16px; /* Button padding */
    border-radius: 4px; /* Rounded corners */
    display: inline-block; /* Display as inline block */
}}

.btn-primary:hover {{
    background-color: #0056b3; /* Button background color on hover */
}}

.btn-primary.disabled {{
    background-color: #ccc; /* Disabled button background color */
    cursor: not-allowed; /* Change cursor on disabled state */
}}
                    

/* Custom CSS for positioning */
.row {{
    display: flex; /* Use flexbox for layout */
}}

.col-left {{
    flex: 1; /* Take up 50%  =of the available space */
    padding-right: 10px; /* Optional: Add some spacing between cards */
}}
.col-middle {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}}                   

.col-right {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}} 
.sub-header{{
    text-align: center ! important;
    font-family:Impact, fantasy!important;                    
}}                                           
</style>

<h1 class="sub-header">Pneumonia Information</h1>
<p class="sub-header">Pneumonia is an infection that inflames the air sacs in one or both lungs, which may fill with fluid or pus. Common causes include bacteria, viruses, and fungi.</p>                    
<div class="row">   
    <div class="col-left">                        
        <div class="card">                
            <img src="data:image/jpeg;base64,{more_info4}" class="card-img-top" alt="Pneumonia Information Image">
            <div class="card-body">
                <h5 class="card-title">More Information</h5>   
                <p class="card-text">
                   Pneumonia is an infection that inflames the air sacs in one or both lungs. The air sacs may fill with fluid or pus, causing symptoms such as a cough, fever, chills, and difficulty breathing.
                    <br>
                    <strong>Pneumonia Overview:</strong> <a href="https://www.who.int/news-room/fact-sheets/detail/pneumonia" target="_blank">More information about pneumonia</a><br>
                </p>
            </div>
        </div>            
    </div>
    <div class="col-middle"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{penu_man}" class="card-img-top" alt="Pneumonia Symptoms Image">
            <div class="card-body">
                <h5 class="card-title">Symptoms</h5>
                <p class="card-text">
                   Symptoms of pneumonia can range from mild to severe and may include chest pain, cough with phlegm, fatigue, fever, sweating, chills, nausea, vomiting, and shortness of breath.
                    <br>
                    <strong>Pneumonia Symptoms:</strong> <a href="https://www.cdc.gov/pneumonia/symptoms-causes.html" target="_blank">Symptoms of Pneumonia</a><br>
                </p>
            </div>
        </div>                  
    </div>                 
    <div class="col-right"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{penu_prev}" class="card-img-top" alt="Pneumonia Prevention Image">
            <div class="card-body">
                <h5 class="card-title">Prevention</h5>
                <p class="card-text">
                    Prevention of pneumonia includes vaccination, practicing good hygiene, quitting smoking, and maintaining a healthy lifestyle. It's also important to manage other health conditions that can increase the risk of pneumonia.
                    <br>
                    <strong>Preventing Pneumonia:</strong> <a href="https://www.cdc.gov/pneumonia/prevention.html" target="_blank">How to prevent Pneumonia</a><br>
                </p>
            </div>
        </div>                  
    </div>                  
</div>"""

penumonia_page_else=f"""
                    <style>
/* Card styling */
.card {{
    width: 500px; /* Adjust width as needed */
    margin: 20px auto; /* Center the card horizontally */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add box shadow */
    border: 1px solid #ddd; /* Add border */
    border-radius: 8px; /* Rounded corners */
    overflow: hidden; /* Prevents image overflow */
    background:rgb(2,0,36,0.7);
                       
    -webkit-mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    mask: url("https://raw.githubusercontent.com/robin-dela/css-mask-animation/master/img/urban-sprite.png");
    -webkit-mask-size: 3000% 100%;
    mask-size: 3000% 100%;                    
}}

.card-img-top {{
    width: 100%; /* Full width image */
    height:200px; /* Maintain aspect ratio */
    object-fit: cover; /* Scale image while maintaining aspect ratio */
}}

.card-body {{
    padding: 20px; /* Padding inside the card body */
    height:200px;                    
}}

.card-title {{
    font-size: 1.25rem; /* Title font size */
    color:white; 
    margin-bottom: 10px; /* Space below title */
}}

.card-text {{
    font-size: 1rem; /* Text font size */
    color:white;                     
    line-height: 1.6; /* Line height */
}}
.card-text a{{
    color:red;
                        
}}

.btn-primary {{
    background-color: #007bff; /* Primary button background color */
    color: #fff; /* Text color */
    text-decoration: none; /* Remove underline */
    padding: 8px 16px; /* Button padding */
    border-radius: 4px; /* Rounded corners */
    display: inline-block; /* Display as inline block */
}}

.btn-primary:hover {{
    background-color: #0056b3; /* Button background color on hover */
}}

.btn-primary.disabled {{
    background-color: #ccc; /* Disabled button background color */
    cursor: not-allowed; /* Change cursor on disabled state */
}}
                    

/* Custom CSS for positioning */
.row {{
    display: flex; /* Use flexbox for layout */
}}

.col-left{{
    flex: 1; /* Take up 50%  =of the available space */
    padding-right: 10px; /* Optional: Add some spacing between cards */
}}

.col-right {{
    flex: 1; /* Take up 50% =of the available space */
    padding-left: 10px; /* Optional: Add some spacing between cards */               
}}
.sub-header{{
    text-align: center ! important;
    font-family:Impact, fantasy!important;                    
}}                                            
</style>
                    
<h1 class="sub-header">Healthy Life Information</h1>
<p class="sub-header">The results indicate that you are not likely to have pneumonia. However, maintaining a healthy lifestyle is crucial for overall respiratory health.</p>                    
<div class="row">   
    <div class="col-left">                        
        <div class="card">                
            <img src="data:image/jpeg;base64,{healthy_lungs}" class="card-img-top" alt="Healthy Lifestyle Tips Image">
            <div class="card-body">
                <h5 class="card-title">Healthy Lifestyle Tips</h5>
                <p class="card-text">
                    A healthy lifestyle plays a crucial role in maintaining overall respiratory health. It involves consuming a balanced diet, staying hydrated, and avoiding smoking and exposure to pollutants.
                    <br>
                    <strong>Tips for a Healthy Lifestyle:</strong> <a href="https://www.lung.org/lung-health-diseases/wellness" target="_blank">Healthy lifestyle tips</a><br>
                </p>
            </div>
        </div>            
    </div>                
    <div class="col-right"> 
        <div class="card">
            <img src="data:image/jpeg;base64,{peaks}" class="card-img-top" alt="Exercise and Respiratory Health Image">
            <div class="card-body">
                <h5 class="card-title">Exercise and Respiratory Health</h5>
                <p class="card-text">
                    Regular physical activity is essential for maintaining physical and mental health. It strengthens the respiratory system and boosts the immune system, helping to prevent infections such as pneumonia.
                    <br>
                    <strong>Exercise and Respiratory Health:</strong> <a href="https://www.cdc.gov/physicalactivity/basics/pa-health/index.htm" target="_blank">Benefits of exercise</a><br>
                </p>
            </div>
        </div>                  
    </div>                  
</div>

"""
history_value=f""" <style>
            .heart-disease-img {{
                width:100%;
                height: 500px !important;
                display: block;
                margin: auto;
    
            }}
            </style>
            <img src="data:image/jpeg;base64,{history}" class="heart-disease-img">
            """
login_image=f""" <style>
            .heart-disease-img {{
                width:100%;
                height: 500px !important;
                display: block;
                margin: auto;
    
            }}
            </style>
            <img src="data:image/jpeg;base64,{login}" class="heart-disease-img">
            """
sign_image=f""" <style>
            .heart-disease-img {{
                width:100%;
                height: 500px !important;
                display: block;
                margin: auto;
    
            }}
            </style>
            <img src="data:image/jpeg;base64,{sign}" class="heart-disease-img">
            """
