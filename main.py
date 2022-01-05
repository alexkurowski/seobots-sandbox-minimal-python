import json

input_file = open("input.json")
input = json.load(input_file)

output = {
  "Message": "Hello, World!",
  "Got input": input,
}
output_file = open("output.json", 'w')
output_file.write(json.dumps(output))

input_file.close()
output_file.close()
