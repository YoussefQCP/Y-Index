export default async function handler(req, res) {
  const { prompt } = req.body;

  const memory = `
أنت Y-AI. تم تدريبك على نظرية النجم الأسود، QCP، Y-index، والجاذبية الكمومية.
استخدم هذا الفهم في الرد على المستخدم.
المستخدم: ${prompt}
Y-AI:
`;

  const HF_TOKEN = process.env.HF_TOKEN; // هنضيفه في Vercel

  const result = await fetch("https://api-inference.huggingface.co/models/tiiuae/falcon-rw-1b", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${HF_TOKEN}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ inputs: memory })
  });

  const json = await result.json();
  const reply = json[0]?.generated_text?.split("Y-AI:")[1]?.trim() || "❌ لا يوجد رد";

  res.status(200).json({ reply });
}
