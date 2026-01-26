/*
  Design: Luminous Gradient Futurism
  - Card grid layout with glassmorphic styling
  - Hover effects with scale and glow
  - Staggered fade-in animations
*/

import { useEffect, useRef, useState } from "react";
import { ExternalLink, BarChart3, Users, TrendingUp } from "lucide-react";

interface Project {
  icon: typeof BarChart3;
  title: string;
  description: string;
  gradient: string;
}

const projects: Project[] = [
  {
    icon: BarChart3,
    title: "Credit Risk Assessment & EDA",
    description:
      "Performed rigorous EDA on loan datasets using Python (Pandas, Seaborn) to identify default indicators. Recommended risk-threshold adjustments for lending strategies.",
    gradient: "from-violet-500/20 to-purple-500/20",
  },
  {
    icon: Users,
    title: "Customer Segmentation (RFM Analysis)",
    description:
      "Analyzed global retailer transaction data using RFM values. Utilized K-Means Clustering to identify high-value segments for targeted retention.",
    gradient: "from-blue-500/20 to-cyan-500/20",
  },
  {
    icon: TrendingUp,
    title: "Global Retail Executive Dashboard",
    description:
      "Designed an interactive Tableau dashboard connected to SQL to track sales and profit margins. Reduced reporting turnaround time by 30%.",
    gradient: "from-cyan-500/20 to-teal-500/20",
  },
];

export default function Projects() {
  const [visibleItems, setVisibleItems] = useState<number[]>([]);
  const sectionRef = useRef<HTMLElement>(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const index = parseInt(entry.target.getAttribute("data-index") || "0");
            setVisibleItems((prev) => Array.from(new Set([...prev, index])));
          }
        });
      },
      { threshold: 0.2 }
    );

    const items = document.querySelectorAll(".project-card");
    items.forEach((item) => observer.observe(item));

    return () => observer.disconnect();
  }, []);

  return (
    <section id="projects" ref={sectionRef} className="relative py-24">
      <div className="container">
        <h2 className="text-5xl md:text-6xl font-bold text-center mb-4 gradient-text">
          Projects
        </h2>
        <div className="w-24 h-1 bg-gradient-to-r from-violet-500 to-cyan-500 mx-auto mb-16"></div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto">
          {projects.map((project, index) => {
            const Icon = project.icon;
            const isVisible = visibleItems.includes(index);

            return (
              <div
                key={index}
                data-index={index}
                className={`project-card transition-all duration-1000 ${
                  isVisible
                    ? "opacity-100 translate-y-0"
                    : "opacity-0 translate-y-10"
                }`}
                style={{ transitionDelay: `${index * 150}ms` }}
              >
                <div
                  className={`glass rounded-3xl p-8 h-full shadow-xl shadow-primary/10 hover:shadow-primary/30 transition-all duration-500 hover:scale-105 border border-transparent hover:border-primary/30 bg-gradient-to-br ${project.gradient} group`}
                >
                  <div className="flex items-start justify-between mb-6">
                    <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-violet-500 to-cyan-500 flex items-center justify-center shadow-lg shadow-primary/30 group-hover:scale-110 transition-transform duration-300">
                      <Icon className="h-8 w-8 text-white" />
                    </div>
                    <ExternalLink className="h-6 w-6 text-foreground/40 group-hover:text-primary transition-colors duration-300" />
                  </div>

                  <h3 className="text-2xl font-bold mb-4 text-foreground group-hover:text-primary transition-colors duration-300">
                    {project.title}
                  </h3>

                  <p className="text-foreground/80 leading-relaxed">
                    {project.description}
                  </p>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Floating decorative elements */}
      <div className="absolute top-1/4 right-10 w-32 h-32 bg-violet-500/5 rounded-full blur-3xl"></div>
      <div className="absolute bottom-1/4 left-10 w-40 h-40 bg-cyan-500/5 rounded-full blur-3xl"></div>
    </section>
  );
}
