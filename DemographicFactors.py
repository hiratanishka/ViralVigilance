import plotly.graph_objects as go
import random

# Data
viruses = [
    'Influenza', 'COVID-19', 'HIV/AIDS', 'Hepatitis A', 'Hepatitis B',
    'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Herpes', 'Measles',
    'Mumps', 'Rubella', 'Varicella', 'Zika Virus', 'Ebola',
    'Dengue Fever', 'Chikungunya', 'Rabies', 'Polio', 'West Nile Virus',
    'Norovirus', 'Rotavirus', 'SARS', 'MERS'
]

regions = [
    'Worldwide', 'Worldwide', 'Sub-Saharan Africa, Southeast Asia, South America', 'Africa, Asia, South America',
    'Africa, Asia, Eastern Europe', 'Eastern Europe, Africa, Asia', 'Mediterranean, Central Asia, Africa',
    'East and South Asia', 'Worldwide', 'Africa, Asia', 'Worldwide', 'Africa, Asia', 'Worldwide',
    'South America, Southeast Asia, Africa', 'West Africa', 'Southeast Asia, South America, Africa',
    'Africa, Asia, Americas', 'Africa, Asia', 'Afghanistan, Pakistan, Nigeria', 'North America, Europe, Africa',
    'Worldwide', 'Worldwide, especially developing countries', 'Asia', 'Middle East'
]

# Coordinates of major regions
region_coords = {
    'Worldwide': {'lat': 0, 'lon': 0},
    'Sub-Saharan Africa': {'lat': -5.0, 'lon': 20.0},
    'Southeast Asia': {'lat': 15.0, 'lon': 100.0},
    'South America': {'lat': -15.0, 'lon': -60.0},
    'Africa': {'lat': 0, 'lon': 20.0},
    'Asia': {'lat': 30.0, 'lon': 100.0},
    'Eastern Europe': {'lat': 55.0, 'lon': 25.0},
    'Mediterranean': {'lat': 35.0, 'lon': 18.0},
    'Central Asia': {'lat': 45.0, 'lon': 65.0},
    'East and South Asia': {'lat': 30.0, 'lon': 110.0},
    'East Asia': {'lat': 35.0, 'lon': 105.0},
    'West Africa': {'lat': 10.0, 'lon': -10.0},
    'North America': {'lat': 45.0, 'lon': -100.0},
    'Middle East': {'lat': 25.0, 'lon': 45.0},
    'Afghanistan': {'lat': 33.0, 'lon': 65.0},
    'Pakistan': {'lat': 30.0, 'lon': 70.0},
    'Nigeria': {'lat': 10.0, 'lon': 8.0},
    'Americas': {'lat': 0.0, 'lon': -80.0},
    'Developing countries': {'lat': 10.0, 'lon': 20.0}
}

# Colors for viruses
colors = {
    'Influenza': '#1f77b4',
    'COVID-19': '#ff7f0e',
    'HIV/AIDS': '#2ca02c',
    'Hepatitis A': '#d62728',
    'Hepatitis B': '#9467bd',
    'Hepatitis C': '#8c564b',
    'Hepatitis D': '#e377c2',
    'Hepatitis E': '#7f7f7f',
    'Herpes': '#bcbd22',
    'Measles': '#17becf',
    'Mumps': '#1f77b4',
    'Rubella': '#ff7f0e',
    'Varicella': '#2ca02c',
    'Zika Virus': '#d62728',
    'Ebola': '#9467bd',
    'Dengue Fever': '#8c564b',
    'Chikungunya': '#e377c2',
    'Rabies': '#7f7f7f',
    'Polio': '#bcbd22',
    'West Nile Virus': '#17becf',
    'Norovirus': '#1f77b4',
    'Rotavirus': '#ff7f0e',
    'SARS': '#2ca02c',
    'MERS': '#d62728'
}

# Create the scattergeo plot
fig = go.Figure()

# Track added virus-region pairs and viruses to avoid duplicates
added_pairs = set()
added_viruses = set()  # Track added viruses for legend

for virus, region in zip(viruses, regions):
    if region == 'Worldwide':
        pair = (virus, 'Worldwide')
        if pair not in added_pairs:
            fig.add_trace(go.Scattergeo(
                lat=[region_coords['Worldwide']['lat'] + random.uniform(-0.5, 0.5)],
                lon=[region_coords['Worldwide']['lon'] + random.uniform(-0.5, 0.5)],
                text=virus + ' (Worldwide)',
                marker=dict(
                    size=10,
                    color=colors[virus],
                    symbol='circle'
                ),
                name=virus if virus not in added_viruses else ''  # Add virus to legend only once
            ))
            added_pairs.add(pair)
            added_viruses.add(virus)
    else:
        for reg in region.split(', '):
            if reg in region_coords:
                pair = (virus, reg)
                if pair not in added_pairs:
                    coords = region_coords[reg]
                    fig.add_trace(go.Scattergeo(
                        lat=[coords['lat']],
                        lon=[coords['lon']],
                        text=virus + ' (' + reg + ')',
                        marker=dict(
                            size=10,
                            color=colors[virus],
                            symbol='square'
                        ),
                        name=virus if virus not in added_viruses else ''  # Add virus to legend only once
                    ))
                    added_pairs.add(pair)
                    added_viruses.add(virus)

# Remove empty legend entries
for trace in fig.data:
    if trace.name == '':
        trace.showlegend = False

# Update layout for the map
fig.update_layout(
    title='Demographic Factors: Regions Most Affected by Different Viruses',
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    )
)

fig.show()
