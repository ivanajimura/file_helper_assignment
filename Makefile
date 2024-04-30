freeze-requirements:
	@pip freeze > requirements.txt

install-requirements:
	@pip install -r requirements.txt

run-tests:		#runs all tests from all files
	@pytest

run-test-file:	# runs all tests from a single file
	@pytest $(path)

run-single-test:	# runs a single test from a file
	@pytest $(path)::$(method)

save-test-report:	# saves report to an xml file
	@pytest --junitxml=$(filename).xml