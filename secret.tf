resource "kubernetes_secret" "my_secret" {
  metadata {
    name      = "my-secret"
    namespace = "orin-terraform"
  }

  data = {
    hafifa = "VHJ1ZQ=="
    name   = "b3Jpbg=="
  }

  type = "Opaque"
}
