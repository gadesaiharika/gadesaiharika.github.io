/*
  Design: Luminous Gradient Futurism
  - Glassmorphic contact card
  - Social links with hover effects
  - Gradient footer
*/

import { Mail, Phone, Linkedin, Github } from "lucide-react";
import { Button } from "@/components/ui/button";

interface ContactLink {
  icon: typeof Mail;
  label: string;
  value: string;
  href: string;
  gradient: string;
}

const contactLinks: ContactLink[] = [
  {
    icon: Mail,
    label: "Email",
    value: "gadesaiharika@gmail.com",
    href: "mailto:gadesaiharika@gmail.com",
    gradient: "from-violet-500 to-purple-600",
  },
  {
    icon: Phone,
    label: "Phone",
    value: "+1 (662) 497-4248",
    href: "tel:+16624974248",
    gradient: "from-blue-500 to-indigo-600",
  },
  {
    icon: Linkedin,
    label: "LinkedIn",
    value: "linkedin.com/in/saiharikagade",
    href: "https://linkedin.com/in/saiharikagade",
    gradient: "from-cyan-500 to-blue-600",
  },
  {
    icon: Github,
    label: "GitHub",
    value: "github.com/gadesaiharika",
    href: "https://github.com/gadesaiharika",
    gradient: "from-teal-500 to-cyan-600",
  },
];

export default function Contact() {
  return (
    <section id="contact" className="relative py-24">
      <div className="container">
        <h2 className="text-5xl md:text-6xl font-bold text-center mb-4 gradient-text">
          Get in Touch
        </h2>
        <div className="w-24 h-1 bg-gradient-to-r from-violet-500 to-cyan-500 mx-auto mb-16"></div>

        <div className="max-w-4xl mx-auto">
          <div className="glass rounded-3xl p-8 md:p-12 shadow-2xl shadow-primary/20">
            <p className="text-xl text-center text-foreground/80 mb-12 leading-relaxed">
              I'm always open to discussing new opportunities, collaborations,
              or just connecting with fellow data enthusiasts. Feel free to
              reach out!
            </p>

            <div className="grid md:grid-cols-2 gap-6">
              {contactLinks.map((link, index) => {
                const Icon = link.icon;

                return (
                  <a
                    key={index}
                    href={link.href}
                    target={link.href.startsWith("http") ? "_blank" : undefined}
                    rel={
                      link.href.startsWith("http")
                        ? "noopener noreferrer"
                        : undefined
                    }
                    className="group"
                  >
                    <div className="flex items-center gap-4 p-6 rounded-2xl bg-gradient-to-br from-primary/10 to-transparent border border-primary/20 hover:border-primary/50 transition-all duration-300 hover:scale-105 hover:shadow-lg hover:shadow-primary/20">
                      <div
                        className={`w-12 h-12 rounded-xl bg-gradient-to-br ${link.gradient} flex items-center justify-center shadow-lg shadow-primary/30 group-hover:scale-110 transition-transform duration-300`}
                      >
                        <Icon className="h-6 w-6 text-white" />
                      </div>
                      <div className="flex-1">
                        <p className="text-sm font-medium text-foreground/70 mb-1">
                          {link.label}
                        </p>
                        <p className="text-foreground font-semibold group-hover:text-primary transition-colors duration-300">
                          {link.value}
                        </p>
                      </div>
                    </div>
                  </a>
                );
              })}
            </div>

            <div className="mt-12 text-center">
              <Button
                size="lg"
                className="bg-gradient-to-r from-violet-600 to-cyan-600 hover:from-violet-700 hover:to-cyan-700 text-white font-semibold shadow-lg shadow-primary/30 transition-all duration-300 hover:scale-105 text-lg px-12 py-6"
                onClick={() =>
                  window.open("mailto:gadesaiharika@gmail.com", "_blank")
                }
              >
                Send me an Email
                <Mail className="ml-2 h-5 w-5" />
              </Button>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="mt-24 border-t border-border/50">
        <div className="container py-8">
          <p className="text-center text-foreground/60">
            © 2026 Sai Harika Gade. Built with passion for data and AI.
          </p>
        </div>
      </footer>
    </section>
  );
}
