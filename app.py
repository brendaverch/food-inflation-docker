import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def main(data_path="CPI_dataset.csv"):

    df = pd.read_csv(data_path)

    print("\n== Leitura do Dataset ==")
    print(f"Formato inicial: {df.shape[0]} linhas, {df.shape[1]} colunas.")
    print("Colunas:", list(df.columns))

    # 2) Remoção de linhas com forecast_percent_change nulo
    df.dropna(subset=["forecast_percent_change"], inplace=True)
    print(f"\nApós remover nulos em 'forecast_percent_change': {df.shape[0]} linhas restantes.")

    # Coluna-alvo
    target_col = "forecast_percent_change"

    # 3) Transformação das colunas categóricas em dummies (one-hot)
    categorical_cols = ["consumer_price_index_item", "month_of_forecast", "attribute"]

    # Realiza one-hot encoding para cada coluna categórica
    # Isso converte cada categoria em uma coluna binária (0 ou 1)
    df = pd.get_dummies(df, columns=categorical_cols)

    print("\n== Depois de One-Hot Encoding ==")
    print(f"Novo formato: {df.shape[0]} linhas, {df.shape[1]} colunas.")

    # 4) Separa em X (features) e y (alvo)
    # Retiramos a coluna 'forecast_percent_change' do X
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # 5) Divisão em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("\n== Divisão Treino/Teste ==")
    print(f"Treino: {X_train.shape[0]} linhas, Teste: {X_test.shape[0]} linhas.")

    # 6) Modelo de Regressão
    regressor = RandomForestRegressor(
        n_estimators=100,  # número de árvores
        random_state=42,
        n_jobs=-1          # usa todos os núcleos de CPU disponíveis
    )
    regressor.fit(X_train, y_train)

    print("\n== Treinamento Concluído ==")

    # 7) Avaliação do Modelo
    y_pred_train = regressor.predict(X_train)
    y_pred_test = regressor.predict(X_test)

    mse_train = mean_squared_error(y_train, y_pred_train)
    mse_test = mean_squared_error(y_test,  y_pred_test)
    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test,  y_pred_test)

    print("\n== Métricas de Desempenho ==")
    print(f"MSE Treino: {mse_train:.4f} | R² Treino: {r2_train:.4f}")
    print(f"MSE Teste:  {mse_test:.4f}  | R² Teste:  {r2_test:.4f}")

    # 8) Exemplo de previsões
    sample_features = X_test.head(5)
    sample_truth = y_test.head(5)
    sample_preds = regressor.predict(sample_features)

    print("\n== Exemplo de Previsões (5 amostras) ==")
    for i in range(len(sample_features)):
        print(f"  - Real: {sample_truth.iloc[i]:.2f} | Previsto: {sample_preds[i]:.2f}")

    print("\nScript finalizado com sucesso!")


if __name__ == "__main__":
    main()
