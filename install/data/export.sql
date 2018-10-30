--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.10
-- Dumped by pg_dump version 9.6.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: catégories; Type: TABLE; Schema: public; Owner: respoweb
--

CREATE TABLE public."catégories" (
    id integer NOT NULL,
    name character varying
);


ALTER TABLE public."catégories" OWNER TO respoweb;

--
-- Name: catégories_id_seq; Type: SEQUENCE; Schema: public; Owner: respoweb
--

CREATE SEQUENCE public."catégories_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."catégories_id_seq" OWNER TO respoweb;

--
-- Name: catégories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: respoweb
--

ALTER SEQUENCE public."catégories_id_seq" OWNED BY public."catégories".id;


--
-- Name: plages_ip; Type: TABLE; Schema: public; Owner: respoweb
--

CREATE TABLE public.plages_ip (
    id integer NOT NULL,
    "id_catégories" integer NOT NULL,
    ip_mask character varying,
    description character varying
);


ALTER TABLE public.plages_ip OWNER TO respoweb;

--
-- Name: plages_ip_id_seq; Type: SEQUENCE; Schema: public; Owner: respoweb
--

CREATE SEQUENCE public.plages_ip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.plages_ip_id_seq OWNER TO respoweb;

--
-- Name: plages_ip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: respoweb
--

ALTER SEQUENCE public.plages_ip_id_seq OWNED BY public.plages_ip.id;


--
-- Name: résultat_scan; Type: TABLE; Schema: public; Owner: respoweb
--

CREATE TABLE public."résultat_scan" (
    id integer NOT NULL,
    id_plages_ip integer NOT NULL,
    ip character varying,
    port character varying,
    state character varying,
    name character varying
);


ALTER TABLE public."résultat_scan" OWNER TO respoweb;

--
-- Name: résultat_scan_id_seq; Type: SEQUENCE; Schema: public; Owner: respoweb
--

CREATE SEQUENCE public."résultat_scan_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."résultat_scan_id_seq" OWNER TO respoweb;

--
-- Name: résultat_scan_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: respoweb
--

ALTER SEQUENCE public."résultat_scan_id_seq" OWNED BY public."résultat_scan".id;


--
-- Name: catégories id; Type: DEFAULT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public."catégories" ALTER COLUMN id SET DEFAULT nextval('public."catégories_id_seq"'::regclass);


--
-- Name: plages_ip id; Type: DEFAULT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public.plages_ip ALTER COLUMN id SET DEFAULT nextval('public.plages_ip_id_seq'::regclass);


--
-- Name: résultat_scan id; Type: DEFAULT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public."résultat_scan" ALTER COLUMN id SET DEFAULT nextval('public."résultat_scan_id_seq"'::regclass);


--
-- Data for Name: catégories; Type: TABLE DATA; Schema: public; Owner: respoweb
--

COPY public."catégories" (id, name) FROM stdin;
\.


--
-- Name: catégories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: respoweb
--

SELECT pg_catalog.setval('public."catégories_id_seq"', 1, false);


--
-- Data for Name: plages_ip; Type: TABLE DATA; Schema: public; Owner: respoweb
--

COPY public.plages_ip (id, "id_catégories", ip_mask, description) FROM stdin;
\.


--
-- Name: plages_ip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: respoweb
--

SELECT pg_catalog.setval('public.plages_ip_id_seq', 1, false);


--
-- Data for Name: résultat_scan; Type: TABLE DATA; Schema: public; Owner: respoweb
--

COPY public."résultat_scan" (id, id_plages_ip, ip, port, state, name) FROM stdin;
\.


--
-- Name: résultat_scan_id_seq; Type: SEQUENCE SET; Schema: public; Owner: respoweb
--

SELECT pg_catalog.setval('public."résultat_scan_id_seq"', 1, false);


--
-- Name: catégories catégories_pkey; Type: CONSTRAINT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public."catégories"
    ADD CONSTRAINT "catégories_pkey" PRIMARY KEY (id);


--
-- Name: plages_ip plages_ip_pkey; Type: CONSTRAINT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public.plages_ip
    ADD CONSTRAINT plages_ip_pkey PRIMARY KEY (id);


--
-- Name: résultat_scan résultat_scan_pkey; Type: CONSTRAINT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public."résultat_scan"
    ADD CONSTRAINT "résultat_scan_pkey" PRIMARY KEY (id);


--
-- Name: résultat_scan résultat_scan_id_plages_ip_fkey; Type: FK CONSTRAINT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public."résultat_scan"
    ADD CONSTRAINT "résultat_scan_id_plages_ip_fkey" FOREIGN KEY (id_plages_ip) REFERENCES public.plages_ip(id);


--
-- PostgreSQL database dump complete
--

