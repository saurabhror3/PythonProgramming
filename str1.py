def main():
  # 1. Prompt user to enter a string
  user_input = input("Enter a string: ")

  # 2. Apply string operations
  upper_str = user_input.upper()
  lower_str = user_input.lower()
  trimmed_str = user_input.strip()

  # Replace substring
  old_sub = input("Enter the substring to replace: ")
  new_sub = input("Enter the new substring: ")
  replaced_str = user_input.replace(old_sub, new_sub)

  # Count character occurrences
  char_to_count = input("Enter a character to count: ")
  count = user_input.count(char_to_count)

  # 3. Display results
  print("\n--- Formatted Results ---")
  print(f"Original string: {user_input}")
  print(f"Uppercase: {upper_str}")
  print(f"Lowercase: {lower_str}")
  print(f"Trimmed: '{trimmed_str}'")
  print(f"Replaced: {replaced_str}")
  print(f"Occurrences of '{char_to_count}': {count}")


# Run the script
main()
