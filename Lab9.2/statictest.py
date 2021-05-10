import pycodestyle

fchecker = pycodestyle.Checker('class_unitTest.py', show_source=True)
file_errors = fchecker.check_all()

print("Found %s errors (and warnings)" % file_errors)

fchecker = pycodestyle.Checker('filecmp_unitTest.py', show_source=True)
file_errors = fchecker.check_all()

print("Found %s errors (and warnings)" % file_errors)

fchecker = pycodestyle.Checker('mathCeil_unitTest.py', show_source=True)
file_errors = fchecker.check_all()

print("Found %s errors (and warnings)" % file_errors)