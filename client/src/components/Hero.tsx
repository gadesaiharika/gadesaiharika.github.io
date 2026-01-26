/*
  Design: Luminous Gradient Futurism
  - Diagonal split composition with hero background
  - Gradient text for name
  - Floating glassmorphic elements
  - Smooth fade-in animations
*/

import { Button } from "@/components/ui/button";
import { ArrowDown, Download, ExternalLink } from "lucide-react";
import { useEffect, useState } from "react";

export default function Hero() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <section
      id="hero"
      className="relative min-h-screen flex items-center justify-center overflow-hidden"
      style={{
        backgroundImage: "url(/images/hero-background.png)",
        backgroundSize: "cover",
        backgroundPosition: "center",
      }}
    >
      {/* Overlay for better text readability */}
      <div className="absolute inset-0 bg-gradient-to-br from-background/95 via-background/80 to-background/95"></div>

      <div className="container relative z-10 py-20">
        <div className="max-w-4xl mx-auto text-center">
          {/* Main content with fade-in animation */}
          <div
            className={`transition-all duration-1000 ${
              isVisible
                ? "opacity-100 translate-y-0"
                : "opacity-0 translate-y-10"
            }`}
          >
            <h1 className="text-6xl md:text-8xl font-bold mb-6 gradient-text">
              Sai Harika Gade
            </h1>

            <p className="text-2xl md:text-3xl font-semibold text-foreground/90 mb-4">
              M.S. Computer Science Candidate
            </p>

            <p className="text-xl md:text-2xl text-foreground/70 mb-8">
              Data Analytics & Machine Learning Specialist
            </p>

            <div className="glass rounded-2xl p-6 mb-12 max-w-3xl mx-auto">
              <p className="text-lg text-foreground/80 leading-relaxed">
                Building scalable data pipelines and bias mitigation frameworks
                for Multimodal AI.
              </p>
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <Button
                size="lg"
                onClick={() => scrollToSection("projects")}
                className="bg-gradient-to-r from-violet-600 to-cyan-600 hover:from-violet-700 hover:to-cyan-700 text-white font-semibold shadow-lg shadow-primary/30 transition-all duration-300 hover:scale-105 text-lg px-8 py-6"
              >
                View Projects
                <ExternalLink className="ml-2 h-5 w-5" />
              </Button>

              <Button
                size="lg"
                variant="outline"
                className="glass border-2 border-primary/50 hover:border-primary text-foreground font-semibold transition-all duration-300 hover:scale-105 text-lg px-8 py-6"
              >
                Download Resume
                <Download className="ml-2 h-5 w-5" />
              </Button>
            </div>
          </div>

          {/* Scroll indicator */}
          <div
            className={`mt-20 transition-all duration-1000 delay-500 ${
              isVisible
                ? "opacity-100 translate-y-0"
                : "opacity-0 translate-y-10"
            }`}
          >
            <button
              onClick={() => scrollToSection("about")}
              className="flex flex-col items-center gap-2 text-foreground/60 hover:text-foreground transition-all duration-300 animate-bounce mx-auto"
            >
              <span className="text-sm font-medium">Scroll to explore</span>
              <ArrowDown className="h-6 w-6" />
            </button>
          </div>
        </div>
      </div>

      {/* Floating decorative elements */}
      <div className="absolute top-1/4 left-10 w-32 h-32 bg-violet-500/10 rounded-full blur-3xl animate-pulse"></div>
      <div className="absolute bottom-1/4 right-10 w-40 h-40 bg-cyan-500/10 rounded-full blur-3xl animate-pulse delay-1000"></div>
    </section>
  );
}
