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
