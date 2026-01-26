/*
  Design: Luminous Gradient Futurism
  - Glassmorphic sticky navigation with backdrop blur
  - Smooth scroll to sections
  - Hover effects with glow
*/

import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";

export default function Navigation() {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${
        isScrolled
          ? "glass shadow-lg shadow-primary/10"
          : "bg-transparent"
      }`}
    >
      <div className="container mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          <button
            onClick={() => scrollToSection("hero")}
            className="text-xl font-bold gradient-text hover:opacity-80 transition-opacity"
          >
            SHG
          </button>

          <div className="hidden md:flex items-center gap-8">
            {["Home", "About", "Experience", "Projects", "Skills", "Contact"].map(
              (item) => (
                <button
                  key={item}
                  onClick={() => scrollToSection(item.toLowerCase())}
                  className="text-sm font-medium text-foreground/80 hover:text-foreground transition-all duration-300 hover:scale-105 relative group"
                >
                  {item}
                  <span className="absolute bottom-0 left-0 w-0 h-0.5 bg-gradient-to-r from-violet-500 to-cyan-500 group-hover:w-full transition-all duration-300"></span>
                </button>
              )
            )}
          </div>

          <Button
            onClick={() => scrollToSection("contact")}
            className="bg-gradient-to-r from-violet-600 to-cyan-600 hover:from-violet-700 hover:to-cyan-700 text-white font-semibold shadow-lg shadow-primary/30 transition-all duration-300 hover:scale-105"
          >
            Get in Touch
          </Button>
        </div>
      </div>
    </nav>
  );
}
