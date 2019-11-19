

from app.model import reconstructed_final_model

if __name__ == "__main__":
    # WARNING!
    # THIS IS A DESTRUCTIVE ACTION THAT WILL OVERWRITE THE MODEL WEIGHTS FILE
    model = reconstructed_final_model(idempotent=False)
    print(type(model))
