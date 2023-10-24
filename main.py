import pandas as pd
import matplotlib.pyplot as plt

#CSV url
url = "https://raw.githubusercontent.com/OscarCabreraRodriguez/bipi-Test/main/customers.csv"

try:
    #Leer el csv mediante la url
    df = pd.read_csv(url)
    #Crear columna gasto
    df['expense'] = (df['Annual Income ($)'] * df['Spending Score (1-100)']) / 100

    #Número y porcentaje sobre el total absoluto de Mujeres monoparentales que han gastado más de 15.000 dólares 
    query_mujeres_df = df.loc[(df['Gender'] == "Female") & (df['expense'] > 15000) & (df['Family Size'] == 1)]
    print("Número de mujeres monoparentales que han gastado más de 15.000$:",len(query_mujeres_df))
    print("Porcentaje de mujeres monoparentales que han gastado más de 15.000$",(len(query_mujeres_df)/len(df))*100)

    #abogados (M/F) hay en el dataset que tengan mayor experiencia laboral que la media de ingenieros hombres
    ingenieros_m_df = df.loc[(df['Gender'] == "Male") & (df['Profession'] == "Engineer")]
    experiencia_ing_m = ingenieros_m_df["Work Experience"].mean()

    abogados_exp_df = df.loc[(df['Profession'] == "Lawyer") & (df["Work Experience"] > experiencia_ing_m)]
    print("Número de abogados con mayor experiencia laboral que la media de ingenieros hombres:", len(abogados_exp_df))

    #Dibuja la distribución de abogados en función de su gasto anual (utiliza franjas de gasto) y de su sexo.
    male_abogados_df = df.loc[(df['Profession'] == "Lawyer") & (df['Gender'] == "Male")]
    female_abogados_df = df.loc[(df['Profession'] == "Lawyer") & (df['Gender'] == "Female")]
    
    #Construcción del gráfico
    fig, axs = plt.subplots(1, 2, tight_layout=True)
    axs[0].hist(female_abogados_df["expense"], alpha=0.5, label="Female")
    axs[1].hist(male_abogados_df["expense"], alpha=0.5, label="Male")

    axs[0].set_xlabel("Gasto Anual")
    axs[0].set_ylabel("Número de Abogados")
    axs[1].set_xlabel("Gasto Anual")
    axs[1].set_ylabel("Número de Abogados")
    
    axs[0].set_title("Female")
    axs[1].set_title("Male")
    fig.suptitle("Distribución de Abogados por Gasto Anual y Sexo")
    
    plt.show()

    #Relación entre años trabajados y salario para los abogados
    print("Ahora estudiaremos si hay una relación entre los años trabajados y el salario de los abogados para ello usaremos un gráfico de dispersión")
    plt.figure(figsize=(10, 6))

    plt.scatter(female_abogados_df['Work Experience'], female_abogados_df['Annual Income ($)'], label='Mujeres', color='red')
    plt.scatter(male_abogados_df['Work Experience'], male_abogados_df['Annual Income ($)'], label='Hombres', color='blue')

    plt.xlabel('Años Trabajados')
    plt.ylabel('Salario Anual ($)')
    plt.title('Relación de Años Trabajados y Salario para Abogados por Género')
    plt.legend()
    plt.grid(True)

    plt.show()

    print("Podemos observar que no hay una relación muy directa entre los años trabajados y el salario")

except Exception as e:
    print(f"An error occurred: {str(e)}")
