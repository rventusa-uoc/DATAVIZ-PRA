import pandas as pd

# Leemos csv
df = pd.read_csv("Suicide Rates Overview (1985 to 2021).csv")

# Calculamos diferencia en PIB per cápita
df["cambio_pib_per_capita"] = df["gdp_per_capita ($)"] - df["gdp_per_capita ($)"].min()

# Buscamos la máxima diferencia
max_pib_per_capita_change = df.groupby("country")["cambio_pib_per_capita"].max()

# Ordenamos de mayor a menor y cogemos los 10 más altos
top_increased_pib_per_capita = (
    max_pib_per_capita_change.sort_values(ascending=False).head(10)
)

# Sacamos valores extremos de años por país
min_max_years = df.groupby("country")[["year"]].agg(
    min_year=pd.NamedAgg(column="year", aggfunc="min"), 
    max_year=pd.NamedAgg(column="year", aggfunc="max")
    )

# Mostramos resultados
print("Países con mayor incremento en PIB per cápita:")
for country, increase in top_increased_pib_per_capita.items():
    min_year = min_max_years.loc[country]["min_year"]
    max_year = min_max_years.loc[country]["max_year"]
    year_range = max_year-min_year
    print(f"- {country} de {min_year} a {max_year} ({year_range} años):")
    print(f"  - Aumento: ${increase:,.2f}")
