import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

cereal_data = pandas.read_csv("{cereal.csv}")