resource "kubernetes_namespace" "orin_terraform" {
  metadata {
    name = "orin-terraform"
  }
}
