resource "kubernetes_config_map" "my_configmap" {
  metadata {
    name      = "my-configmap"
    namespace = "orin-terraform"
  }

  data = {
    facts = <<EOF
- Fact 1: my first name is orin.
- Fact 2: my last name is elbilia.
- Fact 3: I am 19 years old.
EOF
  }
}
