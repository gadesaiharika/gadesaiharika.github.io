/*
  Design: Luminous Gradient Futurism
  - Grid layout with skill categories
  - Glassmorphic cards with hover effects
  - Icons and badges for technologies
*/

import { useEffect, useRef, useState } from "react";
import { Code, Database, BarChart, Cloud } from "lucide-react";

interface SkillCategory {
  icon: typeof Code;
  title: string;
  skills: string[];
  gradient: string;
}

const skillCategories: SkillCategory[] = [
  {
    icon: Code,
    title: "Languages",
    skills: ["Python (Pandas, NumPy)", "SQL (Joins, CTEs)", "Java"],
    gradient: "from-violet-500 to-purple-600",
  },
  {
    icon: BarChart,
    title: "Data & Visualization",
    skills: ["Tableau", "Power BI", "Excel", "Matplotlib", "Seaborn"],
    gradient: "from-blue-500 to-indigo-600",
  },
  {
    icon: Database,
    title: "ML & AI",
    skills: [
      "Scikit-learn",
      "Regression",
      "Classification",
      "NLP",
      "Knowledge Graphs",
    ],
    gradient: "from-cyan-500 to-blue-600",
  },
  {
    icon: Cloud,
    title: "Tools & Cloud",
    skills: ["AWS (S3)", "Git", "Jupyter", "Google Colab"],
    gradient: "from-teal-500 to-cyan-600",
  },
];

export default function Skills() {
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
      id="skills"
      ref={sectionRef}
      className="relative py-24"
      style={{
        backgroundImage: "url(/images/ai-research-visual.png)",
        backgroundSize: "cover",
        backgroundPosition: "center",
      }}
    >
      {/* Overlay */}
      <div className="absolute inset-0 bg-background/92"></div>

      <div className="container relative z-10">
        <h2 className="text-5xl md:text-6xl font-bold text-center mb-4 gradient-text">
          Skills
        </h2>
        <div className="w-24 h-1 bg-gradient-to-r from-violet-500 to-cyan-500 mx-auto mb-16"></div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-7xl mx-auto">
          {skillCategories.map((category, index) => {
            const Icon = category.icon;

            return (
              <div
                key={index}
                className={`transition-all duration-1000 ${
                  isVisible
                    ? "opacity-100 translate-y-0"
                    : "opacity-0 translate-y-10"
                }`}
                style={{ transitionDelay: `${index * 100}ms` }}
              >
                <div className="glass rounded-3xl p-6 h-full shadow-xl shadow-primary/10 hover:shadow-primary/30 transition-all duration-500 hover:scale-105 group">
                  {/* Icon header */}
                  <div
                    className={`w-14 h-14 rounded-2xl bg-gradient-to-br ${category.gradient} flex items-center justify-center mb-6 shadow-lg shadow-primary/30 group-hover:scale-110 transition-transform duration-300`}
                  >
                    <Icon className="h-7 w-7 text-white" />
                  </div>

                  <h3 className="text-xl font-bold mb-4 text-foreground">
                    {category.title}
                  </h3>

                  <div className="flex flex-wrap gap-2">
                    {category.skills.map((skill, i) => (
                      <span
                        key={i}
                        className="px-3 py-1.5 rounded-full text-sm font-medium bg-gradient-to-r from-primary/20 to-accent/20 text-foreground/90 border border-primary/30 hover:border-primary/60 transition-all duration-300 hover:scale-105"
                      >
                        {skill}
                      </span>
                    ))}
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Publications section */}
        <div
          className={`mt-16 max-w-4xl mx-auto transition-all duration-1000 delay-500 ${
            isVisible ? "opacity-100 translate-y-0" : "opacity-0 translate-y-10"
          }`}
        >
          <h3 className="text-3xl font-bold text-center mb-8 text-foreground">
            Publications
          </h3>
          <div className="glass rounded-3xl p-8 shadow-xl shadow-primary/10">
            <p className="text-lg text-foreground/90 leading-relaxed">
              <span className="font-semibold text-primary">
                "Computational Tools for Modeling Respiratory Disease Spread"
              </span>{" "}
              <span className="text-foreground/70">(Under Review)</span>
              <br />
              <span className="text-foreground/80 mt-2 block">
                Co-authored modeling/parallelization sections for poultry
                production simulations.
              </span>
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
