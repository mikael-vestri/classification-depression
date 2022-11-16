import logging
import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    print('hello')
