from flask import render_template, request, jsonify
import ipaddress
from ip_sub_app import app

def get_ip_class(first_octet):
    """Determine the class of the IP address based on its first octet."""
    first_octet = int(first_octet)
    
    if 0 <= first_octet <= 127:
        return "A"
    elif 128 <= first_octet <= 191:
        return "B"
    elif 192 <= first_octet <= 223:
        return "C"
    elif 224 <= first_octet <= 239:
        return "D"
    elif 240 <= first_octet <= 255:
        return "E"
    else:
        return "Unknown"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ip_octet1 = request.form['ip_octet1']
        ip_octet2 = request.form['ip_octet2']
        ip_octet3 = request.form['ip_octet3']
        ip_octet4 = request.form['ip_octet4']
        subnet_mask = request.form['subnet_mask']
        
        ip_address = f"{ip_octet1}.{ip_octet2}.{ip_octet3}.{ip_octet4}"
        
        try:
            network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)
            ip_class = get_ip_class(ip_octet1)
            
            ip = ipaddress.IPv4Address(ip_address)
            
            if ip in network.hosts():
                usable = "Yes"
            else:
                usable = "No"
            
            result = {
                "IP_CLASS": ip_class,
                "GROUP": "Private" if network.is_private else "Public",
                "USABLE": usable,
                "NETWORK_ID": str(network.network_address),
                "BROADCAST_IP": str(network.broadcast_address),
                "SUBNET_MASK": subnet_mask,
                "CIDR_NOTATION": f"/{network.prefixlen}",
                "AVAILABLE_HOSTS": network.num_addresses - 2,  
                "NETWORK_TYPE": "Private" if network.is_private else "Public",
                "IP_RANGE": f"{network.network_address + 1} - {network.broadcast_address - 1}",
                "TOTAL_SUBNETS": 1  
            }
            return jsonify(result)
        except ValueError:
            return jsonify({"error": "Invalid IP or Subnet Mask"})
    
    return render_template('index.html')
