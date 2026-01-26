/*
  Design: Luminous Gradient Futurism
  - Glassmorphic card with backdrop blur
  - Diagonal background accent
  - Fade-in on scroll animation
*/

import { useEffect, useRef, useState } from "react";
import { GraduationCap, Brain, Database } from "lucide-react";

export default function About() {
  const [isVisible, setIsVisible] = useState(false);
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        }
      },
      { threshold: 0.2 }
    );

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => observer.disconnect();
  }, []);

  return (
    <section
      id="about"
      ref={sectionRef}
      className="relative py-24 overflow-hidden"
    >
      {/* Background decoration */}
      <div className="absolute inset-0 opacity-30">
        <div
          className="absolute top-0 right-0 w-1/2 h-full"
          style={{
            backgroundImage: "url(/images/code-pattern-bg.png)",
            backgroundSize: "cover",
            backgroundPosition: "center",
            transform: "rotate(5deg) scale(1.2)",
          }}
        ></div>
      </div>

      <div className="container relative z-10">
        <div
          className={`transition-all duration-1000 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <h2 className="text-5xl md:text-6xl font-bold text-center mb-4 gradient-text">
            About Me
          </h2>
          <div className="w-24 h-1 bg-gradient-to-r from-violet-500 to-cyan-500 mx-auto mb-16"></div>

          <div className="max-w-4xl mx-auto">
            <div className="glass rounded-3xl p-8 md:p-12 shadow-2xl shadow-primary/20">
              <p className="text-lg md:text-xl text-foreground/90 leading-relaxed mb-8">
                I am a Master's candidate at Mississippi State University with a
                4.0 GPA and a strong foundation in Machine Learning and Data
                Analytics. I combine technical rigor with the communication
                skills of a technical mentor to deliver efficient,
                production-ready data solutions. My expertise lies in cleaning
                large-scale datasets, optimizing SQL queries, and developing
                frameworks for AI fairness.
              </p>

              {/* Key highlights */}
              <div className="grid md:grid-cols-3 gap-6 mt-12">
                <div className="flex flex-col items-center text-center p-6 rounded-2xl bg-gradient-to-br from-violet-500/10 to-transparent border border-violet-500/20 hover:border-violet-500/40 transition-all duration-300 hover:scale-105">
                  <GraduationCap className="h-12 w-12 text-violet-400 mb-4" />
                  <h3 className="font-semibold text-lg mb-2">4.0 GPA</h3>
                  <p className="text-sm text-foreground/70">
                    Mississippi State University
                  </p>
                </div>

                <div className="flex flex-col items-center text-center p-6 rounded-2xl bg-gradient-to-br from-blue-500/10 to-transparent border border-blue-500/20 hover:border-blue-500/40 transition-all duration-300 hover:scale-105">
                  <Brain className="h-12 w-12 text-blue-400 mb-4" />
                  <h3 className="font-semibold text-lg mb-2">AI Fairness</h3>
                  <p className="text-sm text-foreground/70">
                    Bias Mitigation Research
                  </p>
                </div>

                <div className="flex flex-col items-center text-center p-6 rounded-2xl bg-gradient-to-br from-cyan-500/10 to-transparent border border-cyan-500/20 hover:border-cyan-500/40 transition-all duration-300 hover:scale-105">
                  <Database className="h-12 w-12 text-cyan-400 mb-4" />
                  <h3 className="font-semibold text-lg mb-2">Data Pipelines</h3>
                  <p className="text-sm text-foreground/70">
                    Production-Ready Solutions
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
