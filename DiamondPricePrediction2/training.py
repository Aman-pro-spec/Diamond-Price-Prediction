import os
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    # 1. Data Ingestion (Data read karega)
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    # 2. Data Transformation (Data clean karke naya preprocessor.pkl banayega)
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # 3. Model Training (Naya model.pkl banayega jo naye version ke saath chalega)
    model_trainer = ModelTrainer()
    model_trainer.initate_model_training(train_arr, test_arr)
    
    print("\nSuccessfully Retrained! New model.pkl and preprocessor.pkl created.")