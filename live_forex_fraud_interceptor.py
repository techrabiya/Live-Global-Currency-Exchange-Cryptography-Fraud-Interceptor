print("--- API Challenge 2 Initialized: Live Forex Gateway 🌐 ---")

def process_live_forex_stream(api_rate_payload, transfer_amount_usd):
    print(f"Consuming live exchange rate for pair: {api_rate_payload.get('currency_pair')}")
    
    conversion_rate = api_rate_payload.get('rate', 83.0)
    converted_inr = transfer_amount_usd * conversion_rate
    
    try:
        if transfer_amount_usd > 100000.0:
            if converted_inr > 8500000.0:
                print("API Compliance Log: Massive high-value institutional wire detected.")
                return "mandatory RBI compliance clearance and source audit"
            else:
                print("API Notice: Large transfer within approved exchange margins.")
                return "institutional tier clearing authorized"
        else:
            print("API Status: Transfer amount within standard retail limits.")
            return "standard cross-border payout approved"
            
    except TypeError:
        print("API Error: Invalid data format in live rate stream.")
        return "forex API data type error handled"

mock_forex_data = {"currency_pair": "USD/INR", "rate": 83.5}
print("\nRunning API Test 2:")
print(process_live_forex_stream(mock_forex_data, 150000.0))
