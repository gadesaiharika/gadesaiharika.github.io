/*
  Design: Luminous Gradient Futurism
  - Vertical timeline with flowing connector lines
  - Glassmorphic cards for each position
  - Staggered fade-in animations
*/

import { useEffect, useRef, useState } from "react";
import { Briefcase, GraduationCap } from "lucide-react";

interface ExperienceItem {
  icon: typeof Briefcase;
  title: string;
  organization: string;
  period: string;
  responsibilities: string[];
}

const experiences: ExperienceItem[] = [
  {
    icon: GraduationCap,
    title: "Graduate Researcher (Bias Auditing & Multimodal AI)",
    organization: "Mississippi State University",
    period: "Aug 2025 – Present",
    responsibilities: [
      "Developing a framework to audit social bias in Multimodal LLMs using Knowledge Graphs (Wikidata) and neural embeddings.",
      "Utilizing statistical fairness metrics (WEAT, Demographic Parity) to quantify bias in high-stakes AI models.",
      "Summarizing complex findings for academic and industry audiences.",
    ],
  },
  {
    icon: GraduationCap,
    title: "Graduate Teaching Assistant (Data Science)",
    organization: "Mississippi State University",
    period: "Jan 2025 – Present",
    responsibilities: [
      "Assisting in advanced coursework (Applied Data Science I & II).",
      "Conducting code reviews and QA for student Python projects, focusing on pipeline efficiency.",
      "Translating technical concepts for non-technical stakeholders.",
    ],
  },
];

export default function Experience() {
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
      { threshold: 0.3 }
    );

    const items = document.querySelectorAll(".experience-item");
    items.forEach((item) => observer.observe(item));

    return () => observer.disconnect();
  }, []);

  return (
    <section
      id="experience"
      ref={sectionRef}
      className="relative py-24 overflow-hidden"
      style={{
        backgroundImage: "url(/images/data-visualization-abstract.png)",
        backgroundSize: "cover",
        backgroundPosition: "center",
      }}
    >
      {/* Overlay */}
      <div className="absolute inset-0 bg-background/90"></div>

      <div className="container relative z-10">
        <h2 className="text-5xl md:text-6xl font-bold text-center mb-4 gradient-text">
          Experience
        </h2>
        <div className="w-24 h-1 bg-gradient-to-r from-violet-500 to-cyan-500 mx-auto mb-16"></div>

        <div className="max-w-4xl mx-auto relative">
          {/* Vertical timeline line */}
          <div className="absolute left-8 md:left-1/2 top-0 bottom-0 w-0.5 bg-gradient-to-b from-violet-500 via-blue-500 to-cyan-500"></div>

          {experiences.map((exp, index) => {
            const Icon = exp.icon;
            const isVisible = visibleItems.includes(index);

            return (
              <div
                key={index}
                data-index={index}
                className={`experience-item relative mb-16 transition-all duration-1000 ${
                  isVisible
                    ? "opacity-100 translate-x-0"
                    : "opacity-0 translate-x-10"
                }`}
                style={{ transitionDelay: `${index * 200}ms` }}
              >
                <div className="flex items-start gap-8">
                  {/* Timeline dot */}
                  <div className="relative z-10 flex-shrink-0">
                    <div className="w-16 h-16 rounded-full glass flex items-center justify-center border-2 border-primary shadow-lg shadow-primary/30">
                      <Icon className="h-8 w-8 text-primary" />
                    </div>
                  </div>

                  {/* Content card */}
                  <div className="flex-1 glass rounded-2xl p-6 md:p-8 shadow-xl shadow-primary/10 hover:shadow-primary/20 transition-all duration-300 hover:scale-[1.02]">
                    <h3 className="text-2xl font-bold mb-2 text-foreground">
                      {exp.title}
                    </h3>
                    <div className="flex flex-col md:flex-row md:items-center gap-2 mb-4">
                      <p className="text-lg font-semibold text-primary">
                        {exp.organization}
                      </p>
                      <span className="hidden md:inline text-foreground/50">•</span>
                      <p className="text-sm text-foreground/70">{exp.period}</p>
                    </div>
                    <ul className="space-y-3">
                      {exp.responsibilities.map((resp, i) => (
                        <li
                          key={i}
                          className="flex items-start gap-3 text-foreground/80"
                        >
                          <span className="text-cyan-400 mt-1">▹</span>
                          <span>{resp}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
