help:
	@echo "    run"
	@echo "        Run the rasa actions."

run:
	python -m rasa_sdk --actions actions
