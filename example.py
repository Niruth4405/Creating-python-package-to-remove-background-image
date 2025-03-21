from bg_remover import remove_background

# Set custom input/output directories if needed
input_folder = "input"
output_folder = "output"

# Run the background removal function
print("Processing images...")
remove_background(input_folder, output_folder)
print("Done!")
