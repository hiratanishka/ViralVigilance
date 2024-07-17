import plotly.graph_objs as go

# Viruses and their affected age groups
viruses = ['Influenza', 'COVID-19', 'HIV/AIDS', 'Hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 
           'Herpes', 'Measles', 'Mumps', 'Rubella', 'Varicella', 'Zika Virus', 'Ebola', 
           'Dengue Fever', 'Chikungunya', 'Rabies', 'Polio', 'West Nile Virus', 'Norovirus', 'Rotavirus', 'SARS', 'MERS']

# Age groups affected
age_groups = ['All ages, especially young children and elderly', 
              'All ages, especially elderly and those with comorbidities', 
              'Adults (25-44 years)', 
              'All ages, especially children', 
              'All ages, especially newborns and adults', 
              'All ages, especially adults', 
              'Adults', 
              'Young adults and adults', 
              'All ages', 
              'Children', 
              'Children and young adults', 
              'Children and young adults', 
              'Children', 
              'All ages, especially pregnant women', 
              'All ages', 
              'All ages, especially children', 
              'All ages', 
              'All ages', 
              'Children', 
              'All ages, especially elderly', 
              'All ages', 
              'Infants and young children', 
              'All ages, especially elderly', 
              'All ages, especially elderly']

# Convert age groups to numerical values for plotting
age_group_values = [3 if 'all ages' in group.lower() else 2 if 'adults' in group.lower() else 1 for group in age_groups]

# Create a bar chart
fig = go.Figure(data=go.Bar(x=viruses, y=age_group_values, text=age_groups, textposition='auto'))
fig.update_layout(title='Comparison of Age Groups Affected by Different Viruses',
                  xaxis_title='Viruses',
                  yaxis_title='Age Group (1=Children, 2=Adults, 3=All Ages)',
                  xaxis_tickangle=-45)

# Show the plot
fig.show()
