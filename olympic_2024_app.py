import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import json
import requests
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(    page_title="OLYMPIC GAMES PARIS 2024",
     layout="centered",
    initial_sidebar_state="expanded",
 )

st.sidebar.image("https://press.paris2024.org/themes/redcurrentsredcurrents/olympics-games/images/assets/paris2024_logo_v2.gif", use_column_width=True)
page = st.sidebar.radio('',['Home', 'Contact Us'])

for _  in range(6):
    st.sidebar.write('####')
        
st.sidebar.write('Made By Ali Guinga, 2024')
st.sidebar.write('All Rights Reserved')


df = pd.read_csv('https://raw.githubusercontent.com/Guinga6/Olympic-Games-Paris-2024/main/data/data_of_medal.csv')
df2 = pd.read_csv("https://raw.githubusercontent.com/Guinga6/Olympic-Games-Paris-2024/main/data/medal_detail_data.csv")
df_icon = pd.read_csv('https://raw.githubusercontent.com/Guinga6/Olympic-Games-Paris-2024/main/data/icon_sport_data.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/Guinga6/Olympic-Games-Paris-2024/main/data/medal_table.csv')
df_bar = pd.read_csv("https://raw.githubusercontent.com/Guinga6/Olympic-Games-Paris-2024/main/data/data_for_bar_chart.csv")




url = "https://lottie.host/52f82930-d172-46ed-8b6e-2cd84f468979/daEwdLdqS0.json"

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  

c1, c2 = st.columns((3,2))

with c1:
    st.title("OLYMPIC GAMES PARIS 2024")

with c2:
    #st.image(r"C:\Users\t480\Desktop\price predection project\paris2024_logo_v2.gif", width=200)
    lottie_animation = load_lottieurl(url)
    st_lottie(lottie_animation, loop=False, height=170, width=170)

if page == 'Home':
     

    tab1, tab2, tab3, tab4 = st.tabs(["Statistics", "Medal Table", "Medal Detail","Visuals"])

    with tab1:

        st.write("###")

        st.subheader('In This Olympic Participate ', divider="green")
        
        info1, info2, info3, info4 = st.columns(4)
        
        with info1:
            
            st.markdown(
                """
                <div style="border: 2px solid #4CAF50;
                    border-width: 2px;
                    padding: 5px;
                    border-radius: 15px; 
                    background-color: #f9f9f9;
                    border-style: dashed;
                    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                    <h4>206 Nation</h4>
                </div>
                """, unsafe_allow_html=True
            )
        with info2:
            
            st.markdown(
                """
                <div style="border: 2px solid #4CAF50;
                    border-width: 2px;
                    padding: 5px;
                    border-radius: 15px; 
                    background-color: #f9f9f9;
                    border-style: dashed;
                    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                    <h4>10,714 Player</h4>
                </div>
                """, unsafe_allow_html=True
            )

        with info3:
          
            st.markdown(
            """
            <div style="
                border: 2px solid #4CAF50; 
                padding: 5px; 
                border-radius: 15px; 
                background-color: #f9f9f9;
                border-style: dashed;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                <h4>50% Men</h4>
            </div>
            """, unsafe_allow_html=True
        )
            
        with info4:
           
            st.markdown(
            """
            <div style="
                border: 2px solid #4CAF50; 
                padding: 5px; 
                border-radius: 15px; 
                background-color: #f9f9f9;
                border-style: dashed;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                <h4> 50% Womem</h4>
            </div>
            """, unsafe_allow_html=True
        )
            
        st.write("####")
        st.subheader('In', divider = 'green')
        info5, info6, info7 = st.columns(3)
        with info5:
            
            st.markdown(
                """
                <div style="border: 2px solid #4CAF50;
                    border-width: 2px;
                    padding: 5px;
                    border-radius: 15px; 
                    background-color: #f9f9f9;
                    border-style: dashed;
                    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                    <h4>329 Event</h4>
                </div>
                """, unsafe_allow_html=True
            )
        with info6:
        
            st.markdown(
                """
                <div style="border: 2px solid #4CAF50;
                    border-width: 2px;
                    padding: 5px;
                    border-radius: 15px; 
                    background-color: #f9f9f9;
                    border-style: dashed;
                    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                    <h4>32 Sport</h4>
                </div>
                """, unsafe_allow_html=True
            )

        with info7:
            st.markdown(
            """
            <div style="
                border: 2px solid #4CAF50; 
                padding: 5px; 
                border-radius: 15px; 
                background-color: #f9f9f9;
                border-style: dashed;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                <h4>48  Disciplines</h4>
            </div>
            """, unsafe_allow_html=True
        )
        st.write('####')
        st.subheader("It Was", divider='green')
        
        info21, info22, info23, info24 = st.columns(4)

        with info21:
            
            st.markdown(
                """
                <div style="border: 2px solid #4CAF50;
                    border-width: 2px;
                    padding: 5px;
                    border-radius: 15px; 
                    background-color: #f9f9f9;
                    border-style: dashed;
                    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                    <h4>1032 Medal</h4>
                </div>
                """, unsafe_allow_html=True
            )
        with info22:
        
            st.markdown(
                """
                <div style="border: 2px solid #4CAF50;
                    border-width: 2px;
                    padding: 5px;
                    border-radius: 15px; 
                    background-color: #f9f9f9;
                    border-style: dashed;
                    box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                    <h4>327 Gold</h4>
                </div>
                """, unsafe_allow_html=True
            )

        with info23:
            st.markdown(
            """
            <div style="
                border: 2px solid #4CAF50; 
                padding: 5px; 
                border-radius: 15px; 
                background-color: #f9f9f9;
                border-style: dashed;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                <h4>322 Silver</h4>
            </div>
            """, unsafe_allow_html=True
        )
            
        with info24:
            st.markdown(
            """
            <div style="
                border: 2px solid #4CAF50; 
                padding: 5px; 
                border-radius: 15px; 
                background-color: #f9f9f9;
                border-style: dashed;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);">
                <h4> 383 Bronze</h4>
            </div>
            """, unsafe_allow_html=True
        )
        
        st.write("####")
        st.subheader("Map - Olympic Competition Venues", divider="green")
        st.image("https://storage.googleapis.com/endurance-apps-liip/media/cache/olympics-games_no_filter_grid_fs/6693ae3dc1dc8890fa0ff287")

    with tab2:
            
        st.write("###")
        # Display the entire dataset as a table
        st.header("Medal Table Overview")
        st.write("------")
        colh1,colh2, colh3, colh4, colh5 = st.columns(5)

        with colh1:
            st.subheader('Country',divider='green')

        with colh2:
            st.image("https://static.files.bbci.co.uk/core/website/assets/static/sport/gold-medal.39480c7008fe241d5426.svg",width=45,  caption='Gold')

        with colh3:
            st.image("https://static.files.bbci.co.uk/core/website/assets/static/sport/silver-medal.b90d266096d3c84d282d.svg",width=45, caption='Silver')

        with colh4:
            st.image("https://static.files.bbci.co.uk/core/website/assets/static/sport/bronze-medal.6474a63d1f4b7d486127.svg",width=45, caption='Bronze')

        with colh5:
            st.image("https://static.files.bbci.co.uk/core/website/assets/static/sport/all-medals.b65f8edcc8c802a24e3f.svg",width=70, caption='Total')

        # Convert the dataframe to a list of lists to hide column names
        data_no_headers = df.drop(columns=['Unnamed: 0', 'url_flag']).values.tolist()

        # Display the data as a table
        st.write("###")


        bcol1,bcol2, bcol3, bcol4, bcol5 = st.columns(5)

        with bcol1:

            url_list = df['url_flag'].tolist()
            name_list = df['name_of_country'].tolist()
            i, j= 0, 0
            for element in url_list:
                j += 1 
                if j < 91:
                    st.image(element, width=35, caption= name_list[i])
                    i += 1
                else:
                    break

        with bcol2:

            gold_list = df['gold_medal'].tolist()
            i = 0
            for element in gold_list:
                i +=1
                if i < 91:
                    st.write("\t" + "\n", element) 
                    st.write("####")
                else:
                    break

        with bcol3:

            silver_list = df['silver_medal'].tolist()
            i = 0
            for element in silver_list:
                i += 1
                if i < 91:
                    st.write(element) 
                    st.write("####")
                else:
                    break

        with bcol4:
            
            bronz_list = df['bronze_medal'].tolist()
            i = 0
            for element in bronz_list:
                i += 1
                if i < 91:
                    st.write(element) 
                    st.write("####")
                else:
                    break

        with bcol5:
            total_list = df['total_medal'].tolist()
            i = 0
            for element in total_list:
                i += 1
                if i < 91:
                    st.write("\t"+"\t", element) 
                    st.write("####")
                else:
                    break

        st.write("##")
        st.header("Countries Did Not Win A Medal:")
        st.write("---")

        df_with_no_medal = df[df['total_medal'] == 0]

        url_list = df_with_no_medal['url_flag'].tolist()

        name_list_with_no_medal = df_with_no_medal['name_of_country'].tolist()

        # Set the number of images per row
        images_per_row = 5

        # Loop through the images in chunks and display them
        for i in range(0, len(url_list), images_per_row):
            columns = st.columns(images_per_row)
            for j, element in enumerate(url_list[i:i + images_per_row]):
                with columns[j]:
                    st.image(element, width=100, caption=name_list_with_no_medal[i + j])  # Adjust width if needed

    with tab3:

        df_icon = df_icon.drop(['Unnamed: 0'],axis = 1 )
        df2 = df2.drop(['Unnamed: 0'], axis = 1 )


        c1, c2 = st.columns(2)
        with c1:
            sport_name = st.selectbox(
                'Chose Sport',
                df2['name_of_sport'].unique()
            )
        df_sport = df2[df2['name_of_sport'] == sport_name]
        with c2:
            event_name = st.selectbox(
                'Chose Event',
                df_sport['event_name'].unique()
        )
    
        col1, col2 = st.columns((2,5))

        with col1:
            df_icon = df_icon[df_icon['sport_name'] == sport_name]

            st.subheader(sport_name, divider = 'green')
            for _ in range(2):
                st.write("####")
            
            st.image(df_icon['sport_icon'].to_list()[0], width=190)

        with col2:
            if event_name is None:
                print('')

            else:
                df_sport = df2[df2['name_of_sport'] == sport_name]
                df_event = df_sport[df_sport['event_name'] == event_name]

                st.subheader(df_event['event_name'].to_list()[0], divider='green')
                col1, col2, col3 = st.columns((1,1,3))

                with col1:
                    for icon in df_event['medal_icon'].to_list():
                        st.write('#')
                        st.image(icon, width=35)
                with col2:
                    for flag in df_event['country_flag'].to_list():
                        st.write('#')
                        st.image(flag, width=70)
                with col3:
                    for player in df_event['player_name'].to_list():
                        st.write('#')
                        st.subheader(player)


    with tab4:
        
        st.write("###")
        d1, d2 = st.columns(2)

        gold = df['gold_medal'].to_list()
        silver = df['silver_medal'].to_list()
        bronz = df['bronze_medal'].to_list()
        total = df['total_medal'].to_list()

        with d1:
            c1, c2 = st.columns((1,3))
            with c1:
                st.image(df['url_flag'].to_list()[0], use_column_width=True)
            with c2:
                st.subheader("1. Usa Achivement", divider='blue')

            labels = ['Gold', 'Silver', 'Bronze']
            values = [gold[0], silver[0], bronz[0]]
            colors = ['#FFD700', '#C0C0C0', '#CD7F32']

            # Create a pie chart with a hole to make it a donut chart
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.6, marker=dict(colors=colors))])

            # Update layout to center the chart
            fig.update_traces(textinfo='value', textfont_size=20, marker=dict(line=dict(color='white', width=7)))


            fig.update_layout(
                    annotations=[dict(text=f'{total[0]} Medal', x=0.5, y=0.5, font_size=20, showarrow=False)],
                    showlegend=True,
                    autosize=True,
                    width=500,  # Set the width of the chart
                    height=400 )
            # Streamlit app
                    
            st.plotly_chart(fig, use_container_width=True)

        with d2:

            c1, c2 = st.columns((1,3))
            with c1:
                st.image(df['url_flag'].to_list()[1], use_column_width=True)
            with c2:
                st.subheader("2. China Achivement", divider='red')

            labels = ['Gold', 'Silver', 'Bronze']
            values = [gold[1], silver[1], bronz[1]]
            colors = ['#FFD700', '#C0C0C0', '#CD7F32']

            # Create a pie chart with a hole to make it a donut chart
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.6, marker=dict(colors=colors))])

            # Update layout to center the chart
            fig.update_traces(textinfo='value', textfont_size=20, marker=dict(line=dict(color='white', width=7)))


            fig.update_layout(
                    annotations=[dict(text=f'{total[1]} Medal', x=0.5, y=0.5, font_size=20, showarrow=False)],
                    showlegend=True,
                    autosize=True,
                    width=500,  # Set the width of the chart
                    height=400 )
            # Streamlit app
                    
            st.plotly_chart(fig, use_container_width=True)
        

        country_name = st.selectbox(
                'Your country is not here',
                df3['countries']
            )
        
        df_country = df3[df3['countries'] == country_name]

        c1, c2, c3 = st.columns((1,3,3))
        with c1:
            st.image(df_country['url_flag'].to_list()[0], use_column_width=True)
        with c2:
            #st.write(' ')
            st.subheader(f'{country_name} Achivement', divider='blue')
        with c3:
            st.empty()

        gold1 = df_country['gold_medal'].to_list()
        silver1 = df_country['silver_medal'].to_list()
        bronz1 = df_country['bronze_medal'].to_list()
        total1 = df_country['total_medal'].to_list()

        labels = ['Gold', 'Silver', 'Bronze']
        values = [gold1[0], silver1[0], bronz1[0]]
        colors = ['#FFD700', '#C0C0C0', '#CD7F32']

            # Create a pie chart with a hole to make it a donut chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.6, marker=dict(colors=colors))])

            # Update layout to center the chart
        fig.update_traces(textinfo='value', textfont_size=20, marker=dict(line=dict(color='white', width=7)))


        fig.update_layout(
                    annotations=[dict(text=f'{total1[0]} Medal', x=0.5, y=0.5, font_size=20, showarrow=False)],
                    showlegend=True,
                    autosize=False,)
            # Streamlit app
                    
        st.plotly_chart(fig, use_container_width=True)

       
        # Sort the DataFrame if needed
        
        df_bar = df_bar.drop(['Unnamed: 0'], axis = 1)
        df_bar = df_bar.iloc[0:60, :]
        
        # Create the stacked bar plot using Plotly
        fig = px.bar(df_bar, x="countries", y="medal", color="medal type", barmode="stack",
                    labels={"Value": "medal", "Country": "countries", "Metric": "medal type"},
                    text_auto=True,
                    color_discrete_sequence=["#FFD700", "#C0C0C0", "#CD7F32"])  # This adds value labels to each section of the bar

        # Customize the layout to increase the figure size and adjust the bar width
        fig.update_layout(
            xaxis_title="Countries",
            yaxis_title="No. of Medals",
            template="plotly_white",  # Use a white template for the plot
            width=800,  # Increase the width of the entire figure
            height=600,  # Increase the height of the entire figure
        )

        st.subheader('The Ranking of Some Countries', divider='blue')
        # Display the plot in Streamlit
        st.plotly_chart(fig)




if page == 'Contact Us':

    st.write("--------")
    # Use local CSS
    st.markdown("""<style>/* CSS Snippet from W3schools: https://www.w3schools.com/howto/howto_css_contact_form.asp */
          /* Style inputs with type="text", select elements and textareas */
          input[type=message], input[type=email], input[type=text], textarea {
            width: 100%; /* Full width */
            padding: 12px; /* Some padding */ 
            border: 1px solid #ccc; /* Gray border */
            border-radius: 4px; /* Rounded borders */
            box-sizing: border-box; /* Make sure that padding and width stays in place */
            margin-top: 6px; /* Add a top margin */
            margin-bottom: 16px; /* Bottom margin */
            resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
          }
          
          /* Style the submit button with a specific background color etc */
          button[type=submit] {
            background-color: #04AA6D;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
          }
          
          /* When moving the mouse over the submit button, add a darker green color */
          button[type=submit]:hover {
            background-color: #45a049;
          }
          /* Hide Streamlit Branding */
          #MainMenu {visibility: hidden;}
          footer {visibility: hidden;}
          header {visibility: hidden;}</style>""", unsafe_allow_html = True)
         
    st.header("Get In Touch With Us!", divider='green')
    st.write("#")

    contact_form = """
                <form action="https://formsubmit.co/aliguinga2020@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
                </form> 
                """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

        st.write('###')
        st.write('###')
        st.subheader('Support Us On')
        st.write("----")

        c1, c2 = st.columns(2)

        social = ["https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png", "https://upload.wikimedia.org/wikipedia/commons/e/ef/Youtube_logo.png","https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg","https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"]

        with c1:
            for s in social:
                st.image(s, width = 70)

        with c2:
            
            st.write('#####')
            st.subheader("[Linkedin](https://www.linkedin.com/in/ali-guinga-43770820b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
            st.write('#####')
            st.subheader("[Youtube](https://youtube.com/@aliguinga660?si=gY3OHsIILx6dl_Bi)")
            st.write('#####')
            st.subheader("[Github](https://github.com/Guinga6)")
            st.write('#####')
            st.subheader("[WathsApp](https://wa.me/message/EYMGX25FNHCNN1)") 
                
               

   
    with right_column:
        st.empty()

