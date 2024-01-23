

all: help


run:
	streamlit run app.py --server.runOnSave true

lint:
	flake8 .


help:
	@echo "No Help description yet!"
