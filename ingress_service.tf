resource "kubernetes_service" "ingress_nginx_controller" {
  metadata {
    name      = "ingress-nginx-controller"
    namespace = "orin-terraform"
    labels = {
      app = "ingress-nginx"
    }
  }

  spec {
    selector = {
      app = "ingress-nginx"
    }

    port {
      name        = "http"
      protocol    = "TCP"
      port        = 80
      target_port = 80
    }

    port {
      name        = "https"
      protocol    = "TCP"
      port        = 443
      target_port = 443
    }

    type = "NodePort"
  }
}
