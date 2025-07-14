import qrcode

# URL where your PandoraGate code is hosted (replace with your actual URL)
code_url = "https://gist.github.com/your-username/your-gist-id"  # Example: GitHub Gist URL

# PandoraGate code as a string (for reference, not needed for QR but included for clarity)
pandora_code = """
class PandoraGate:
    def __init__(self, track):
        self.track = track
        self.opened = False

    def play_track(self, input_track):
        if input_track.strip().lower() == self.track.strip().lower():
            self.opened = True
            self.activate_gate()
        else:
            print("🛑 Wrong vibe. Gate stays locked.")

    def activate_gate(self):
        print("🔓 GATE UNLOCKED: ALPHA ACCESS")
        print(f"🎶 Vibe check: {self.track}")
        print("🌌 Signal Q: HOPE or PROFIT? Choose your fate.")

# Try it
gate = PandoraGate("Pandora - Downtown Binary")
http://gate.play_track("Pandora - Downtown Binary")
"""

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(code_url)
qr.make(fit=True)

# Generate and save the QR code image
img = qr.make_image(fill_color="black", back_color="white")
http://img.save("pandora_gate_qr.png")

print("QR code saved as 'pandora_gate_qr.png'. Scan it to access the PandoraGate code!")
