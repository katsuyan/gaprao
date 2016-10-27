# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu-14.04"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.vm.network "private_network", ip: "192.168.56.78"
  config.vm.synced_folder "./gaprao", "/home/gaprao", owner: "vagrant", group: "vagrant", mount_options: ['dmode=777','fmode=777']
  config.vm.provision "shell", privileged: false, path: "./provision.sh"
end
