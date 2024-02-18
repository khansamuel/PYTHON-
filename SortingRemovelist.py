def sort_and_remove_duplicates(names):
  """
  Sorts a list of names alphabetically, removes duplicates, and returns the results.

  Args:
    names: A list of names.

  Returns:
    A tuple containing:
      * A list of sorted names without duplicates.
      * The total number of names entered.
  """
  unique_names = list(set(names))
  unique_names.sort()
  return unique_names, len(names)

# Get names from the user
names = []
while True:
  name = input("Enter a name (or leave blank to finish): ")
  if not name:
    break
  names.append(name)

# Sort and remove duplicates
unique_names, total_names = sort_and_remove_duplicates(names)

# Print the results
print("Unique names (sorted):")
for name in unique_names:
  print(name)
print(f"Total names entered: {total_names}")
