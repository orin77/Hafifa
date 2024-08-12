resource "kubernetes_deployment" "ingress_nginx_controller" {
  metadata {
    name      = "ingress-nginx-controller"
    namespace = "orin-terraform"
    labels = {
      app = "ingress-nginx"
    }
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "ingress-nginx"
      }
    }

    template {
      metadata {
        labels = {
          app = "ingress-nginx"
        }
      }

      spec {
        container {
          name  = "controller"
          image = "quay.io/kubernetes-ingress-controller/nginx-ingress-controller:0.33.0"

          port {
            name          = "http"
            container_port = 80
          }

          port {
            name          = "https"
            container_port = 443
          }

          args = [
            "/nginx-ingress-controller",
            "--configmap=orin/nginx-configuration",
            "--default-backend-service=orin/default-http-backend"
          ]
        }

        service_account_name = "default"
      }
    }
  }
}
