BASEDIR?= logs
LOG_TRACK=--file_storage=$(BASEDIR)

analysis: classifiers
	@echo "done"

features:
	@echo "Generating features"
	# python3 feature_extraction/data_loader.py 

classifiers: svc
	@echo "Finished all classifiers"

svc: features
	python3 experimentation/svc.py $(LOG_TRACK)