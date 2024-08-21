resource "kubernetes_service" "nginx_service" {
  metadata {
    name      = "nginx-service"
    namespace = "orin-terraform"
  }

  spec {
    selector = {
      app = "nginx"
    }

    port {
      protocol    = "TCP"
      port        = 80
      target_port = 80
      node_port   = 30002
    }

    type = "NodePort"
  }
}
