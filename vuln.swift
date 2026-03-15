import Foundation
import WebKit

class VulnerableSwift {
    func storeSecret() {
        // 1. Hardcoded Secret (Real-looking Stripe Key)
        let api_key = "sk_live_51MZpY2LzV9abcd1234567890abcdef1234567890abcdef1234567890"
        let password = "super-secret-password-123"
        UserDefaults.standard.set(api_key, forKey: "APIKey")
    }

    func insecureRandom() {
        // 2. Insecure Randomness
        let random = arc4random()
        print(random)
    }

    func sqlInjection(userInput: String) {
        // 3. Potential SQL Injection
        let query = "SELECT * FROM users WHERE name = '\(userInput)'"
        print(query)
    }

    func insecureWebView() {
        // 4. Insecure WebView config
        let webView = WKWebView()
        webView.configuration.preferences.javaScriptEnabled = true
    }
}
