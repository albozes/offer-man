import csv
import subprocess
import json
import os

# Load rates from CSV file
def load_rates(csv_path):
	rates = []
	with open(csv_path, mode='r') as file:
		csv_reader = csv.reader(file)
		headers = next(csv_reader)
		for row in csv_reader:
			rates.append(dict(zip(headers, row)))
	return rates

# Generate a rate recommendation using Ollama with Llama 3 8B
def generate_rate_recommendation(client_request, rates):
	# Format the prompt
	prompt = f"Client request: {client_request}\n\nHere are the current rates:\n\n"
	for rate in rates:
		rate_description = ", ".join(f"{key}: {value}" for key, value in rate.items())
		prompt += f"- {rate_description}\n"

	prompt += "\nFirst, break down the client request into bullet points for project format, duration, and usage rights. Then, based on the above rates and the client request, please provide a rate recommendation with a short explanation of how you came to that conclusion using the CSV. Next, write a rate suggestion from my perspective that I can send to my client. This should again briefly summarize what they asked for, as include a concrete offer, not a price range. It is vital that this last part is in the language of their original request had, because the client will otherwise not understand me!"

	print("Running the model...")
	# Use subprocess to call Ollama locally with the custom model
	try:
		result = subprocess.run(
			['ollama', 'run', 'rate_model'],
			input=prompt.encode('utf-8'),
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		)

		# Capture standard output and error
		output = result.stdout.decode('utf-8').strip()
		error = result.stderr.decode('utf-8').strip()

		# Print error for debugging, if any
		if error:
			print(f"Error from Ollama: {error}")

		if error and not output:
			return "An error occurred while generating the rate recommendation."

		# If the output is not valid JSON, return it directly
		try:
			response = json.loads(output)
			return response['text'].strip()
		except json.JSONDecodeError:
			return output

	except Exception as e:
		return str(e)

# Main function
def main():
	# Get the directory of the current script
	script_dir = os.path.dirname(__file__)
	# Define the CSV file path
	csv_file_path = os.path.join(script_dir, 'voiceover_rates.csv')
	# Define the Modelfile path
	modelfile_path = os.path.join(script_dir, 'Modelfile')

	# Load the rates from the CSV file
	rates = load_rates(csv_file_path)

	# Check if the model exists
	model_exists = subprocess.run(['ollama', 'list'], stdout=subprocess.PIPE).stdout.decode('utf-8')
	if 'rate_model' not in model_exists:
		print("Creating the model using the Modelfile...")
		subprocess.run(['ollama', 'create', 'rate_model', '-f', modelfile_path])

	# Get the client request
	client_request = input("Please enter the client request: ")

	# Generate the rate recommendation
	rate_recommendation = generate_rate_recommendation(client_request, rates)

	# Output the rate recommendation
	print("\nRate Recommendation:")
	print(rate_recommendation)

if __name__ == "__main__":
	main()
