resource "kubernetes_ingress" "nginx_ingress" {
  metadata {
    name      = "nginx-ingress"
    namespace = "orin-terraform"
  }

  spec {
    rule {
      host = "my-nginx.com"

      http {
        path {
          path = "/"

          backend {
            service_name = "nginx-service"
            service_port = 80
          }
        }
      }
    }
  }
}
