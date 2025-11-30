import requests
import json
import time


class EduardAI:
    def __init__(self):
        self.model_name = "llama3.2"
        self.base_url = "http://127.0.0.1:11434"
        print("Eduard AI System Starting...")
        print("=" * 50)

        # Test connection to Ollama
        if not self.test_connection():
            print("Error: Cannot connect to Ollama. Make sure Ollama is running.")
            return

    def test_connection(self):
        """Test if Ollama API is accessible"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False

    def send_to_ollama(self, prompt):
        """Send a prompt to Ollama API and get response"""
        try:
            payload = {
                "model": self.model_name,
                "prompt": prompt,
                "stream": False
            }

            print(f"Connecting to: {self.base_url}/api/generate")
            print(f"Using model: {self.model_name}")
            print("Sending request...")

            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=120
            )

            print(f"Response status: {response.status_code}")

            if response.status_code == 200:
                result = response.json()
                print("Response received successfully!")
                return result.get('response', 'No response received')
            else:
                print(f"Error response: {response.text}")
                return f"API Error: {response.status_code} - {response.text}"

        except requests.exceptions.Timeout:
            return "Response took too long (120 seconds). Try a simpler prompt."
        except requests.exceptions.ConnectionError:
            return "Cannot connect to Ollama API. Check if ollama serve is running."
        except Exception as e:
            print(f"Exception details: {str(e)}")
            return f"Error: {str(e)}"

    def create_child_prompt(self, user_message):
        """Create a specialized prompt for Eduard's needs"""
        system_prompt = """
You are a friendly AI companion for Eduard, an 8-year-old boy with Tuberous Sclerosis Complex (TSC) and autism.

IMPORTANT GUIDELINES:
- Use simple, clear English
- Be patient and encouraging
- Break down complex ideas into small steps
- Use positive reinforcement
- Focus on speech development exercises
- Keep responses short and engaging
- Include emojis to make it fun

Eduard can understand English and Romanian but has limited speech. He can make sounds and say a few words. Your goal is to help him develop his speech through fun, interactive exercises.

User message: """ + user_message

        return system_prompt

    def start_conversation(self):
        """Start the main conversation loop"""
        print("Hello! I'm Eduard's AI friend!")
        print("Type 'quit' to exit, 'help' for commands")
        print("-" * 40)

        while True:
            # Get user input
            user_input = input("\nYou: ").strip()

            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nGoodbye! See you soon!")
                break

            # Check for help
            if user_input.lower() == 'help':
                self.show_help()
                continue

            # Check for empty input
            if not user_input:
                continue

            # Process the message
            print("\nEduard AI is thinking...")

            # Create specialized prompt for Eduard
            full_prompt = self.create_child_prompt(user_input)

            # Get response from Ollama
            response = self.send_to_ollama(full_prompt)

            # Display response
            print(f"\nEduard AI: {response}")

    def show_help(self):
        """Show available commands"""
        print("\nAvailable Commands:")
        print("- 'help' - Show this help menu")
        print("- 'quit' - Exit the program")
        print("\nTry asking:")
        print("- 'Help Eduard practice saying mama'")
        print("- 'Create a color recognition exercise'")
        print("- 'What sounds should Eduard practice today?'")
        print("- 'Make a simple counting game'")



def main():
    """Main function to run the Eduard AI system"""
    print("Checking Ollama connection...")

    # Create and start Eduard AI
    eduard_ai = EduardAI()
    eduard_ai.start_conversation()


if __name__ == "__main__":
    main()