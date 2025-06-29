import pandas as pd
df = pd.read_csv('/content/diseases(1).csv')

class diseases:
    def __init__(self, dataset_path):
       self.data = pd.read_csv('/content/diseases(1).csv')
    def get_diseases_info(self, tag):
        diseases = self.data[self.data['tag'].str.lower() == tag.lower()]
        if not diseases.empty:
            return diseases.to_dict(orient='records')[0]
        else:
            return None

    def respond_to_query(self, query):
        Tag = query.strip().lower()  # User input converted to lowercase and assigned to 'Tag'
        diseases_info = self.get_diseases_info(Tag)  # Get diseases information based on 'Tag'
        if diseases_info:
            response_text=(f"\n**{diseases_info['tag']}**:\n"
                    f"- bot: {diseases_info['patterns__001']}\n"
                    f"- bot: {diseases_info['patterns__002']}\n"
                    f"- bot: {diseases_info['patterns__003']}\n"
                    f"- bot: {diseases_info['patterns__004']}\n"
                    f"- bot: {diseases_info['patterns__005']}\n"
                    f"- bot: {diseases_info['patterns__006']}\n"
                    f"- bot: {diseases_info['patterns__007']}\n"

                    f"\n- Solution-: {diseases_info['responses__-']}\n")
            for line in response_text.split('.' or '1'):
              print(line)

        else:
            unique_tags = ', '.join(self.data['tag'].unique())
            print("\nBot:Sorry, I don't have information about that disease.\n")

# Load the chatbot
chatbot = diseases('/content/diseases(1).csv')
# Sample interaction
   # Get unique values from the 'tag' column
unique_tags = df['tag'].unique()

# Print the unique tags
for tag in unique_tags:
    print(tag)


while True:

  user_input = input("Bot: Ask about a diseases(or type 'exit' to quit): ").lower()
  print("\nUser:"+user_input)

  if user_input.lower() == 'exit' :
    print("\nBot: BYE BYE\n")
    break

  chatbot.respond_to_query(user_input)
