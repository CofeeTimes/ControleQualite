# ControleQualite
This Project is using rocky linux.  
  
First authorize ssh:  

https://www.tecmint.com/open-port-for-specific-ip-address-in-firewalld/  
https://www.servers.com/support/knowledge/linux-administration/how-to-limit-ssh-access-by-ip-addresses-using-firewall  

And download vscode (https://linuxstoney.com/install-visual-studio-code-on-rocky-linux-8-centos8/#:~:text=The%20easiest%20and%20recommended%20way%20to%20install%20Visual,latest%20version%20of%20Visual%20Studio%20Code%20by%20typing%3A):
```
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc  
sudo vi /etc/yum.repos.d/vscode.repo  
    copy: [code]   
          name=Visual Studio Code  
          baseurl=https://packages.microsoft.com/yumrepos/vscode  
          enabled=1  
          gpgcheck=1  
          gpgkey=https://packages.microsoft.com/keys/microsoft.asc  
sudo dnf install code
```
