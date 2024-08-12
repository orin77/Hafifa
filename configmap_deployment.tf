resource "kubernetes_deployment" "nginx_deployment" {
  metadata {
    name      = "nginx-deployment"
    namespace = "orin-terraform"
  }

  spec {
    replicas = 1

    selector {
      match_labels = {
        app = "nginx"
      }
    }

    template {
      metadata {
        labels = {
          app = "nginx"
        }
      }

      spec {
        container {
          name  = "nginx"
          image = "nginx:latest"

          volume_mount {
            name       = "config-volume"
            mount_path = "/etc/config"
            read_only  = true
          }
        }

        volume {
          name = "config-volume"

          config_map {
            name = "my-configmap"

            items {
              key  = "facts"
              path = "facts.txt"
              mode = "0444"
            }
          }
        }
      }
    }
  }
}
