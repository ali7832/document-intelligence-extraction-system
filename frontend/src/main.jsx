import React, { useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { Activity, Archive, BadgeCheck, ClipboardCheck, Database, Download, FileCheck2, FileSearch, Gauge, Layers3, Search, ShieldCheck, UploadCloud } from 'lucide-react';
import { Area, AreaChart, Bar, BarChart, CartesianGrid, Cell, Pie, PieChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import './styles.css';

const pages = ['Overview', 'Extraction Lab', 'Review Queue', 'Validation', 'Search', 'Exports', 'Audit'];
const qualityTrend = [{d:'Mon',processed:420,review:38},{d:'Tue',processed:510,review:42},{d:'Wed',processed:560,review:31},{d:'Thu',processed:610,review:28},{d:'Fri',processed:690,review:24}];
const docMix = [{name:'Invoices',value:46,color:'#38bdf8'},{name:'Contracts',value:24,color:'#a78bfa'},{name:'Receipts',value:18,color:'#22c55e'},{name:'Forms',value:12,color:'#f59e0b'}];
const queue = [
  ['EXT-9001','invoice_acme.pdf','Invoice','82%','Needs vendor validation'],
  ['EXT-9002','contract_renewal.pdf','Contract','91%','Ready to export'],
  ['EXT-9003','receipt_4481.png','Receipt','68%','Human review required'],
  ['EXT-9004','tax_form.pdf','Form','88%','Check date field']
];
const audit = [
  ['09:10','EXT-9001','classified as invoice','docintel-v1'],
  ['09:11','EXT-9001','extracted total_amount and vendor','extractor'],
  ['09:12','EXT-9003','flagged low confidence','review_router'],
  ['09:18','EXT-9002','exported JSON bundle','operator']
];

function fallbackExtract(form){
  const isInvoice = form.text.toLowerCase().includes('invoice') || form.text.toLowerCase().includes('amount');
  const confidence = isInvoice ? 0.91 : 0.72;
  return {
    extraction_id:`EXT-${Date.now().toString().slice(-5)}`,
    document_type:isInvoice?'invoice':'general_document',
    confidence,
    review_required: confidence < 0.85,
    processing_ms: isInvoice ? 148 : 226,
    fields: isInvoice ? { vendor:'Acme Hospitality Supplies', invoice_number:'INV-2048', total_amount:'$4,820.00', due_date:'2026-06-15' } : { title:'Unclassified business document', detected_language:'English', key_topic:'operations' },
    recommended_action: confidence < 0.85 ? 'Route to human review before export.' : 'Approve structured extraction and export to downstream system.',
  };
}

function App(){
  const [active,setActive] = useState('Overview');
  const [form,setForm] = useState({ document_name:'invoice_acme.pdf', tenant_id:'enterprise-alpha', text:'Invoice INV-2048 from Acme Hospitality Supplies. Total amount $4,820.00 due 2026-06-15.' });
  const [result,setResult] = useState(fallbackExtract(form));
  const metrics = useMemo(()=>[
    ['Documents Processed','48.9K','+19%',FileCheck2],['Straight-Through Rate','86.4%','+8%',BadgeCheck],['Review Queue','124','-31 today',ClipboardCheck],['Avg Confidence','91.2%','+4.2%',Gauge]
  ],[]);
  const extract = async()=>{
    try{
      const response = await fetch('/extract',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(form)});
      if(!response.ok) throw new Error('offline');
      setResult(await response.json());
    }catch{setResult(fallbackExtract(form));}
  };
  return <main className="app-shell"><aside className="sidebar"><div className="brand"><FileSearch/><div><strong>DocIntel AI</strong><span>Document Extraction Cloud</span></div></div>{pages.map(p=><button className={active===p?'active':''} onClick={()=>setActive(p)} key={p}>{p}</button>)}</aside><section className="workspace"><header className="topbar"><div><p className="eyebrow">Enterprise document intelligence</p><h1>{active}</h1></div><button onClick={extract}>Run extraction</button></header>{active==='Overview'&&<Overview metrics={metrics}/>} {active==='Extraction Lab'&&<ExtractionLab form={form} setForm={setForm} result={result} extract={extract}/>} {active==='Review Queue'&&<ReviewQueue/>} {active==='Validation'&&<Validation result={result}/>} {active==='Search'&&<SearchPage/>} {active==='Exports'&&<Exports/>} {active==='Audit'&&<Audit/>}</section></main>
}
function Overview({metrics}){return <><section className="metrics">{metrics.map(([l,v,d,Icon])=><article className="card" key={l}><Icon/><span>{l}</span><strong>{v}</strong><small>{d}</small></article>)}</section><section className="grid"><Panel title="Processing trend" icon={<Activity/>}><ResponsiveContainer width="100%" height={260}><AreaChart data={qualityTrend}><CartesianGrid strokeDasharray="3 3" stroke="#26374a"/><XAxis dataKey="d" stroke="#9badc1"/><YAxis stroke="#9badc1"/><Tooltip/><Area dataKey="processed" stroke="#38bdf8" fill="#0e7490"/><Area dataKey="review" stroke="#fb7185" fill="#7f1d1d"/></AreaChart></ResponsiveContainer></Panel><Panel title="Document mix" icon={<Layers3/>}><ResponsiveContainer width="100%" height={260}><PieChart><Pie data={docMix} dataKey="value" nameKey="name" outerRadius={92}>{docMix.map(d=><Cell key={d.name} fill={d.color}/>)}</Pie><Tooltip/></PieChart></ResponsiveContainer></Panel></section></>}
function ExtractionLab({form,setForm,result,extract}){return <section className="grid"><Panel title="Document input" icon={<UploadCloud/>}><label>Document name<input value={form.document_name} onChange={e=>setForm({...form,document_name:e.target.value})}/></label><label>Tenant ID<input value={form.tenant_id} onChange={e=>setForm({...form,tenant_id:e.target.value})}/></label><label>Document text<textarea value={form.text} onChange={e=>setForm({...form,text:e.target.value})}/></label><button onClick={extract}>Extract fields</button></Panel><Panel title="Extraction result" icon={<FileCheck2/>}><div className="score"><span className={result.review_required?'review':'approved'}>{result.review_required?'review required':'approved'}</span><strong>{Math.round(result.confidence*100)}%</strong><p>{result.document_type} · {result.processing_ms}ms</p><small>{result.extraction_id}</small></div>{Object.entries(result.fields||{}).map(([k,v])=><div className="field" key={k}><span>{k.replaceAll('_',' ')}</span><strong>{v}</strong></div>)}<div className="reason">{result.recommended_action}</div></Panel></section>}
function ReviewQueue(){return <Panel title="Human review queue" icon={<ClipboardCheck/>}><Table rows={queue}/></Panel>}
function Validation({result}){return <section className="grid"><Panel title="Validation rules" icon={<ShieldCheck/>}><div className="reason">Invoice total must be numeric and non-empty.</div><div className="reason">Due date must match accepted date format.</div><div className="reason">Vendor field must map to known supplier or review queue.</div></Panel><Panel title="Current extraction checks" icon={<BadgeCheck/>}><div className="score"><span className={result.review_required?'review':'approved'}>{result.review_required?'needs review':'valid'}</span><strong>{Object.keys(result.fields||{}).length}</strong><p>structured fields extracted</p></div></Panel></section>}
function SearchPage(){return <section className="grid"><Panel title="Document search" icon={<Search/>}><div className="searchbox">Search invoices, contracts, receipts, forms...</div><div className="reason">invoice_acme.pdf · Invoice · 91% confidence</div><div className="reason">contract_renewal.pdf · Contract · 88% confidence</div><div className="reason">receipt_4481.png · Receipt · 68% confidence</div></Panel><Panel title="Indexed metadata" icon={<Database/>}><div className="reason">Tenant, source, document name, submitter, type, confidence, and extraction ID are indexed for review workflows.</div></Panel></section>}
function Exports(){return <section className="grid"><Panel title="Export center" icon={<Download/>}><div className="reason">JSON export bundle ready for invoice_acme.pdf.</div><div className="reason">CSV batch export generated for finance review.</div><div className="reason">Webhook delivery queued for downstream ERP.</div></Panel><Panel title="Downstream systems" icon={<Archive/>}><div className="reason">ERP ingestion</div><div className="reason">Finance approval workflow</div><div className="reason">Compliance archive</div></Panel></section>}
function Audit(){return <Panel title="Extraction audit trail" icon={<Activity/>}><Table rows={audit}/></Panel>}
function Table({rows}){return <div className="table">{rows.map(row=><div className="row" key={row.join('-')}>{row.map(cell=><span key={cell}>{cell}</span>)}</div>)}</div>}
function Panel({title,icon,children}){return <article className="panel"><div className="panel-title">{icon}<h2>{title}</h2></div>{children}</article>}

createRoot(document.getElementById('root')).render(<App/>);
