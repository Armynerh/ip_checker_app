document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('ipUtility');

  form.addEventListener('submit', function(event) {
    event.preventDefault();

    const ip_octet1 = document.getElementById('ip_octet1').value;
    const ip_octet2 = document.getElementById('ip_octet2').value;
    const ip_octet3 = document.getElementById('ip_octet3').value;
    const ip_octet4 = document.getElementById('ip_octet4').value;
    const subnet_mask = document.getElementById('subnet_mask').value;

    const formData = new FormData();
    formData.append('ip_octet1', ip_octet1);
    formData.append('ip_octet2', ip_octet2);
    formData.append('ip_octet3', ip_octet3);
    formData.append('ip_octet4', ip_octet4);
    formData.append('subnet_mask', subnet_mask);

    fetch('/', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        alert(data.error);
      } else {
        // Update the accordion details with response data
        document.getElementById('Ip-Class').textContent = data.IP_CLASS;
        document.getElementById('Ip-Class-Details').textContent = data.IP_CLASS;
        document.getElementById('Ip-Group').textContent = data.GROUP;
        document.getElementById('Ip-Usable').textContent = data.USABLE;
        document.getElementById('Network-ID').textContent = data.NETWORK_ID;
        document.getElementById('Broadcast-IP').textContent = data.BROADCAST_IP;

        document.getElementById('Subnet-Mask').textContent = `255.255.255.${subnet_mask}`;
        document.getElementById('Subnet-CIDR').textContent = data.CIDR_NOTATION;
        document.getElementById('Hosts-Count').textContent = data.AVAILABLE_HOSTS;

        document.getElementById('Network-Type').textContent = data.NETWORK_TYPE;
        document.getElementById('IP-Range').textContent = data.IP_RANGE;
        document.getElementById('Total-Subnets').textContent = data.TOTAL_SUBNETS;
      }
    })
    .catch(error => console.error('Error:', error));
  });
});
