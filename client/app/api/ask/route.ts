import { NextRequest, NextResponse } from "next/server";

const fastApiUrl = process.env.FASTAPI_URL ?? "http://127.0.0.1:8000";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const response = await fetch(`${fastApiUrl}/api/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
      cache: "no-store",
    });

    const responseBody = await response.json();
    return NextResponse.json(responseBody, { status: response.status });
  } catch {
    return NextResponse.json(
      { detail: "Could not connect to the application server." },
      { status: 502 },
    );
  }
}