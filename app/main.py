from transformers import TextClassificationPipeline, BertForSequenceClassification,BertTokenizer,ConvBertForSequenceClassification,ConvBertTokenizer,DistilBertForSequenceClassification,DistilBertTokenizer
import uvicorn
from fastapi import FastAPI
import pandas as pd 


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Yapay Zeka Tabanlı Siber Zorbalık Tespiti"}


@app.post("/predict_bert/")
async def predictBERT(text: str):
    bertModel = BertForSequenceClassification.from_pretrained("app/model/bert")
    bertTokenizer = BertTokenizer.from_pretrained("app/tokenizer/bert")
    pipe= TextClassificationPipeline(model=bertModel, tokenizer=bertTokenizer)
    predictions = pipe(text)

    return {text: predictions}


@app.post("/predict_convBERT/")
async def predictConvBERT(text: str):
    convbertModel = ConvBertForSequenceClassification.from_pretrained("app/model/convbert")
    convbertTokenizer = ConvBertTokenizer.from_pretrained("app/tokenizer/convbert")

    pipe= TextClassificationPipeline(model=convbertModel, tokenizer=convbertTokenizer)
    predictions = pipe(text)

    return {text: predictions}



@app.post("/predict_distilBERT/")
async def predictDistilBERT(text: str):

    distilbertModel = DistilBertForSequenceClassification.from_pretrained("app/model/distilbert")
    distilbertTokenizer = DistilBertTokenizer.from_pretrained("app/tokenizer/distilbert")
    pipe= TextClassificationPipeline(model=distilbertModel, tokenizer=distilbertTokenizer)
    predictions = pipe(text)

    return {text: predictions}


if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port =8000)
